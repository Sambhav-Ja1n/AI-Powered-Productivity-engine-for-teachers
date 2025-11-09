"""
Feature 2: Personalized Content Recommender & Q/A Agent
Simple RAG with vector embeddings + Groq LLM
"""

import os
from groq import Groq
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Tuple
import json

class ContentRecommender:
    def __init__(self, api_key: str, model: str):
        """Initialize content recommender with RAG capabilities"""
        self.client = Groq(api_key=api_key)
        self.model = model
        self.embedding_model = None
        self.knowledge_base = []
        self.embeddings = None
        
    def initialize_embeddings(self):
        """Initialize sentence transformer for embeddings"""
        if self.embedding_model is None:
            print("Loading embedding model...")
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        return self.embedding_model
    
    def add_learning_resources(self, resources: List[Dict]):
        """Add learning resources to knowledge base
        
        Each resource should have:
        - topic: str
        - content: str
        - resource_type: str (video, article, worksheet, etc.)
        - difficulty: str (beginner, intermediate, advanced)
        - teaching_method: str (visual, interactive, discussion, etc.)
        """
        self.knowledge_base.extend(resources)
        
        # Generate embeddings for all resources
        model = self.initialize_embeddings()
        texts = [f"{r['topic']} {r['content']}" for r in self.knowledge_base]
        self.embeddings = model.encode(texts)
        
        print(f"Added {len(resources)} resources. Total: {len(self.knowledge_base)}")
    
    def find_similar_resources(self, query: str, top_k: int = 5) -> List[Dict]:
        """Find most relevant resources using semantic similarity"""
        if not self.knowledge_base:
            return []
        
        model = self.initialize_embeddings()
        query_embedding = model.encode([query])[0]
        
        # Calculate cosine similarity
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        
        # Get top K indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            resource = self.knowledge_base[idx].copy()
            resource['similarity_score'] = float(similarities[idx])
            results.append(resource)
        
        return results
    
    def recommend_content(self, topic: str, student_level: str = "intermediate", 
                         teaching_method: str = None, num_recommendations: int = 3) -> List[Dict]:
        """Recommend personalized learning content"""
        
        # Build search query
        query = f"{topic} {student_level}"
        if teaching_method:
            query += f" {teaching_method}"
        
        # Find similar resources
        similar_resources = self.find_similar_resources(query, top_k=10)
        
        # Filter by criteria
        filtered = similar_resources
        if teaching_method:
            filtered = [r for r in filtered if teaching_method.lower() in r.get('teaching_method', '').lower()]
        
        # Use LLM to rank and explain recommendations
        resources_text = "\n".join([
            f"- {r['topic']} ({r['resource_type']}, {r['difficulty']}): {r['content'][:100]}..."
            for r in filtered[:num_recommendations]
        ])
        
        prompt = f"""Based on these learning resources about "{topic}" for a {student_level} student:

{resources_text}

Explain why each resource is recommended and how it can help the student learn effectively.
Format as JSON array with explanations."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an educational content curator helping personalize learning."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=800
            )
            
            explanation = response.choices[0].message.content
            
        except Exception as e:
            explanation = f"Error getting recommendations: {str(e)}"
        
        # Return top recommendations with explanations
        recommendations = filtered[:num_recommendations]
        return {
            "recommendations": recommendations,
            "explanation": explanation
        }
    
    def answer_question(self, question: str, context_topic: str = None) -> Dict:
        """Answer subject-related questions using RAG"""
        
        # Find relevant resources
        search_query = question
        if context_topic:
            search_query = f"{context_topic} {question}"
        
        relevant_resources = self.find_similar_resources(search_query, top_k=3)
        
        # Build context from resources
        context = "\n\n".join([
            f"Resource: {r['topic']}\n{r['content']}"
            for r in relevant_resources
        ])
        
        prompt = f"""You are a knowledgeable teacher answering student questions.

Question: {question}

Relevant Learning Materials:
{context}

Provide a clear, simple, and accurate answer. Use the learning materials as reference but explain in an easy-to-understand way suitable for students.
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful teacher who explains concepts clearly and simply."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=600
            )
            
            answer = response.choices[0].message.content
            
            return {
                "answer": answer,
                "sources": [r['topic'] for r in relevant_resources],
                "confidence": "high" if relevant_resources else "low"
            }
            
        except Exception as e:
            return {
                "answer": f"Error answering question: {str(e)}",
                "sources": [],
                "confidence": "none"
            }
    
    def generate_practice_worksheet(self, topic: str, difficulty: str, 
                                    num_questions: int = 5) -> Dict:
        """Generate practice questions for a topic"""
        
        prompt = f"""Generate a practice worksheet for students.

Topic: {topic}
Difficulty: {difficulty}
Number of Questions: {num_questions}

Create {num_questions} practice questions with answers. Include:
- Multiple choice questions
- Short answer questions
- One application problem

Format as JSON:
{{
    "title": "<worksheet title>",
    "questions": [
        {{
            "question": "<question text>",
            "type": "<mcq/short/application>",
            "answer": "<answer>",
            "explanation": "<brief explanation>"
        }}
    ]
}}
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert educator creating engaging practice materials."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            result_text = response.choices[0].message.content
            
            try:
                start_idx = result_text.find('{')
                end_idx = result_text.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = result_text[start_idx:end_idx]
                    worksheet = json.loads(json_str)
                else:
                    raise ValueError("No JSON found")
            except:
                worksheet = {
                    "title": f"{topic} Practice Worksheet",
                    "questions": [{"question": result_text, "type": "general", "answer": "", "explanation": ""}]
                }
            
            return worksheet
            
        except Exception as e:
            return {
                "title": "Error",
                "questions": [{"question": f"Error: {str(e)}", "type": "error", "answer": "", "explanation": ""}]
            }


# Sample knowledge base for demo
SAMPLE_RESOURCES = [
    {
        "topic": "Photosynthesis",
        "content": "Photosynthesis is the process by which plants convert light energy into chemical energy. It occurs in chloroplasts and requires sunlight, water, and carbon dioxide. The products are glucose and oxygen.",
        "resource_type": "article",
        "difficulty": "beginner",
        "teaching_method": "visual",
        "url": "https://www.khanacademy.org/science/biology/photosynthesis-in-plants"
    },
    {
        "topic": "Algebra Basics",
        "content": "Introduction to algebraic expressions, variables, and solving simple equations. Learn how to manipulate equations and solve for unknown values using basic operations.",
        "resource_type": "video",
        "difficulty": "beginner",
        "teaching_method": "interactive",
        "url": "https://www.youtube.com/watch?v=NybHckSEQBI"
    },
    {
        "topic": "Newton's Laws of Motion",
        "content": "The three fundamental laws of classical mechanics: law of inertia, F=ma, and action-reaction pairs. Essential for understanding mechanics and motion.",
        "resource_type": "worksheet",
        "difficulty": "intermediate",
        "teaching_method": "discussion",
        "url": "https://www.physicsclassroom.com/class/newtlaws"
    },
    {
        "topic": "Cell Biology",
        "content": "Understanding cell structure, organelles, and their functions. Covers prokaryotic and eukaryotic cells, cell membrane, nucleus, mitochondria, and cellular processes.",
        "resource_type": "article",
        "difficulty": "intermediate",
        "teaching_method": "visual",
        "url": "https://www.khanacademy.org/science/biology/structure-of-a-cell"
    },
    {
        "topic": "Quadratic Equations",
        "content": "Methods for solving quadratic equations including factoring, completing the square, and the quadratic formula. Applications in real-world problem solving.",
        "resource_type": "video",
        "difficulty": "advanced",
        "teaching_method": "interactive",
        "url": "https://www.youtube.com/watch?v=i7idZfS8t8w"
    },
    {
        "topic": "Cellular Respiration",
        "content": "Learn about cellular respiration, glycolysis, Krebs cycle, and electron transport chain. Understand how cells convert glucose into ATP energy.",
        "resource_type": "article",
        "difficulty": "intermediate",
        "teaching_method": "visual",
        "url": "https://www.khanacademy.org/science/biology/cellular-respiration-and-fermentation"
    },
    {
        "topic": "Python Programming",
        "content": "Introduction to Python programming for beginners. Learn variables, loops, functions, and basic data structures through interactive examples.",
        "resource_type": "video",
        "difficulty": "beginner",
        "teaching_method": "interactive",
        "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"
    },
    {
        "topic": "World War II History",
        "content": "Comprehensive overview of World War II causes, major battles, key figures, and global impact. Includes primary sources and historical analysis.",
        "resource_type": "article",
        "difficulty": "intermediate",
        "teaching_method": "discussion",
        "url": "https://www.britannica.com/event/World-War-II"
    }
]


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("LLAMA_MODEL", "llama-3.3-70b-versatile")
    
    recommender = ContentRecommender(api_key, model)
    recommender.add_learning_resources(SAMPLE_RESOURCES)
    
    # Test recommendations
    result = recommender.recommend_content("photosynthesis", "beginner", num_recommendations=2)
    print("Recommendations:")
    print(json.dumps(result, indent=2))
