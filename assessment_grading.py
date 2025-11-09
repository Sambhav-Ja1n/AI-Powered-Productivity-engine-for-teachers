"""
Feature 1: AI Assessment & Grading Assistant
Uses Gemini Vision API for handwriting recognition + Groq LLM for grading
"""

import os
from groq import Groq
from PIL import Image
import google.generativeai as genai
import base64
from typing import Dict, List, Tuple
import json
import io

class AssessmentGradingAssistant:
    def __init__(self, api_key: str, model: str, gemini_api_key: str = None):
        """Initialize the grading assistant with Groq API and Gemini Vision"""
        self.client = Groq(api_key=api_key)
        self.model = model
        self.gemini_api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        
        # Initialize Gemini if API key is available
        if self.gemini_api_key:
            genai.configure(api_key=self.gemini_api_key)
            self.vision_model = genai.GenerativeModel('gemini-2.5-flash')
        else:
            self.vision_model = None
    
    def extract_text_from_image(self, image_path: str) -> str:
        """Extract text from handwritten/printed image using Gemini Vision API"""
        try:
            if not self.vision_model:
                return "Error: Gemini API key not configured"
            
            # Load image with proper context management
            with Image.open(image_path) as img:
                # Create prompt for text extraction
                prompt = """Please extract all the text from this image. 
                This appears to be student homework or an assignment.
                Return ONLY the text content you see, preserving the structure and formatting as much as possible.
                Do not add any commentary or explanation."""
                
                # Generate content with vision model
                response = self.vision_model.generate_content([prompt, img])
                
                extracted_text = response.text.strip()
                return extracted_text
            
        except Exception as e:
            return f"Error extracting text with Gemini Vision: {str(e)}"
    
    def grade_homework(self, student_answer: str, correct_answer: str, 
                       subject: str, max_score: int = 10) -> Dict:
        """Grade homework using Groq LLM"""
        
        prompt = f"""You are an expert teacher grading student homework.

Subject: {subject}
Maximum Score: {max_score}

Correct Answer/Solution:
{correct_answer}

Student's Answer:
{student_answer}

Please evaluate the student's answer and provide:
1. Score (out of {max_score})
2. Detailed feedback
3. Strengths in the answer
4. Areas for improvement
5. Common mistakes identified

Return your response in JSON format:
{{
    "score": <number>,
    "percentage": <percentage>,
    "feedback": "<detailed feedback>",
    "strengths": ["<strength1>", "<strength2>"],
    "improvements": ["<improvement1>", "<improvement2>"],
    "mistakes": ["<mistake1>", "<mistake2>"]
}}
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert educational assessment assistant. Provide fair, constructive feedback."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            result_text = response.choices[0].message.content
            
            # Try to parse JSON from response
            try:
                # Find JSON in the response
                start_idx = result_text.find('{')
                end_idx = result_text.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = result_text[start_idx:end_idx]
                    result = json.loads(json_str)
                else:
                    raise ValueError("No JSON found in response")
            except:
                # Fallback to text response
                result = {
                    "score": max_score // 2,
                    "percentage": 50.0,
                    "feedback": result_text,
                    "strengths": [],
                    "improvements": [],
                    "mistakes": []
                }
            
            return result
            
        except Exception as e:
            return {
                "score": 0,
                "percentage": 0.0,
                "feedback": f"Error grading: {str(e)}",
                "strengths": [],
                "improvements": [],
                "mistakes": []
            }
    
    def grade_from_image(self, image_path: str, correct_answer: str, 
                        subject: str, max_score: int = 10) -> Dict:
        """Complete pipeline: OCR + Grading"""
        
        # Step 1: Extract text from image
        extracted_text = self.extract_text_from_image(image_path)
        
        if extracted_text.startswith("Error"):
            return {
                "score": 0,
                "percentage": 0.0,
                "feedback": extracted_text,
                "extracted_text": "",
                "strengths": [],
                "improvements": [],
                "mistakes": []
            }
        
        # Step 2: Grade the extracted text
        grading_result = self.grade_homework(extracted_text, correct_answer, subject, max_score)
        grading_result["extracted_text"] = extracted_text
        
        return grading_result
    
    def provide_self_evaluation_hints(self, student_answer: str, subject: str) -> Dict:
        """Provide hints for student self-evaluation without giving away answers"""
        
        prompt = f"""You are helping a student self-evaluate their homework.

Subject: {subject}
Student's Answer:
{student_answer}

Provide helpful hints and guidance WITHOUT revealing the correct answer:
1. What aspects they should double-check
2. Key concepts to review
3. Potential areas of concern
4. Self-reflection questions

Return response in JSON format:
{{
    "estimated_score_range": "<range like 6-8/10>",
    "hints": ["<hint1>", "<hint2>"],
    "review_topics": ["<topic1>", "<topic2>"],
    "reflection_questions": ["<question1>", "<question2>"]
}}
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a supportive tutor helping students learn through guided self-evaluation."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=800
            )
            
            result_text = response.choices[0].message.content
            
            try:
                start_idx = result_text.find('{')
                end_idx = result_text.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = result_text[start_idx:end_idx]
                    result = json.loads(json_str)
                else:
                    raise ValueError("No JSON found")
            except:
                result = {
                    "estimated_score_range": "N/A",
                    "hints": [result_text],
                    "review_topics": [],
                    "reflection_questions": []
                }
            
            return result
            
        except Exception as e:
            return {
                "estimated_score_range": "N/A",
                "hints": [f"Error: {str(e)}"],
                "review_topics": [],
                "reflection_questions": []
            }


if __name__ == "__main__":
    # Test the grading assistant
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("LLAMA_MODEL", "llama-3.3-70b-versatile")
    
    assistant = AssessmentGradingAssistant(api_key, model)
    
    # Test text grading
    student_ans = "Photosynthesis is the process where plants convert sunlight into energy using chlorophyll."
    correct_ans = "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to produce oxygen and energy in the form of glucose."
    
    result = assistant.grade_homework(student_ans, correct_ans, "Biology", 10)
    print("Grading Result:")
    print(json.dumps(result, indent=2))
