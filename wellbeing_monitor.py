"""
Feature 3: Teacher Well-being Monitor & Peer Support Hub
Sentiment analysis + AI-powered interventions
"""

import os
from groq import Groq
from datetime import datetime, timedelta
from typing import Dict, List
import json

class WellbeingMonitor:
    def __init__(self, api_key: str, model: str):
        """Initialize wellbeing monitoring system"""
        self.client = Groq(api_key=api_key)
        self.model = model
        self.reflections_history = []
        
    def analyze_sentiment(self, reflection_text: str) -> Dict:
        """Analyze teacher's reflection using Groq LLM"""
        
        prompt = f"""You are a supportive wellbeing coach analyzing a teacher's reflection.

Teacher's Reflection:
"{reflection_text}"

Analyze the emotional tone and wellbeing indicators. Provide:
1. Sentiment score (-1 to 1, where -1 is very negative, 0 is neutral, 1 is very positive)
2. Stress level (low/medium/high)
3. Key emotions detected
4. Wellbeing concerns (if any)
5. Positive aspects mentioned

Return as JSON:
{{
    "sentiment_score": <number between -1 and 1>,
    "stress_level": "<low/medium/high>",
    "emotions": ["<emotion1>", "<emotion2>"],
    "concerns": ["<concern1>", "<concern2>"],
    "positive_aspects": ["<positive1>", "<positive2>"],
    "overall_assessment": "<brief summary>"
}}
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an empathetic wellbeing analyst trained to detect stress and emotional patterns in teachers."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=800
            )
            
            result_text = response.choices[0].message.content
            
            try:
                start_idx = result_text.find('{')
                end_idx = result_text.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = result_text[start_idx:end_idx]
                    analysis = json.loads(json_str)
                else:
                    raise ValueError("No JSON found")
            except:
                analysis = {
                    "sentiment_score": 0.0,
                    "stress_level": "medium",
                    "emotions": [],
                    "concerns": [],
                    "positive_aspects": [],
                    "overall_assessment": result_text
                }
            
            # Store reflection
            self.reflections_history.append({
                "timestamp": datetime.now().isoformat(),
                "reflection": reflection_text,
                "analysis": analysis
            })
            
            return analysis
            
        except Exception as e:
            return {
                "sentiment_score": 0.0,
                "stress_level": "unknown",
                "emotions": [],
                "concerns": [f"Error: {str(e)}"],
                "positive_aspects": [],
                "overall_assessment": f"Error analyzing reflection: {str(e)}"
            }
    
    def provide_micro_intervention(self, sentiment_analysis: Dict) -> Dict:
        """Suggest personalized micro-interventions based on analysis"""
        
        stress_level = sentiment_analysis.get('stress_level', 'medium')
        concerns = sentiment_analysis.get('concerns', [])
        emotions = sentiment_analysis.get('emotions', [])
        
        prompt = f"""You are a wellbeing coach providing supportive interventions for a teacher.

Current State:
- Stress Level: {stress_level}
- Emotions: {', '.join(emotions)}
- Concerns: {', '.join(concerns)}

Provide 3-5 practical micro-interventions that can be done quickly (5-15 minutes) to improve wellbeing. Include:
- Quick relaxation techniques
- Mindfulness exercises
- Time management tips
- Self-care suggestions
- When to seek peer support

Format as JSON:
{{
    "priority": "<low/medium/high>",
    "interventions": [
        {{
            "title": "<intervention name>",
            "description": "<what to do>",
            "duration": "<time needed>",
            "benefit": "<expected benefit>"
        }}
    ],
    "seek_support": <true/false>,
    "support_message": "<message about seeking help if needed>"
}}
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a compassionate wellbeing coach specializing in teacher mental health."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=1000
            )
            
            result_text = response.choices[0].message.content
            
            try:
                start_idx = result_text.find('{')
                end_idx = result_text.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = result_text[start_idx:end_idx]
                    interventions = json.loads(json_str)
                else:
                    raise ValueError("No JSON found")
            except:
                interventions = {
                    "priority": "medium",
                    "interventions": [{"title": "Reflection", "description": result_text, "duration": "5 min", "benefit": "General wellbeing"}],
                    "seek_support": False,
                    "support_message": ""
                }
            
            return interventions
            
        except Exception as e:
            return {
                "priority": "medium",
                "interventions": [{"title": "Error", "description": str(e), "duration": "N/A", "benefit": "N/A"}],
                "seek_support": False,
                "support_message": ""
            }
    
    def get_peer_support_suggestions(self, concern_type: str) -> List[Dict]:
        """Suggest peer support connections based on concerns"""
        
        prompt = f"""A teacher is experiencing concerns related to: {concern_type}

Provide 5-6 practical peer support suggestions. For each suggestion, provide:
- A clear action they can take
- Who to connect with
- What to discuss

Format your response as a numbered list with clear, actionable items.
Keep it concise and friendly."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a supportive colleague helping teachers connect with peers. Provide clear, friendly, actionable advice in a numbered list format. Be specific and practical."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=600
            )
            
            suggestions_text = response.choices[0].message.content
            
            # Convert newlines to HTML breaks for better display
            suggestions_html = suggestions_text.replace('\n', '<br>')
            
            # Return as structured data
            return {
                "concern_type": concern_type,
                "suggestions": suggestions_html
            }
            
        except Exception as e:
            return {
                "concern_type": concern_type,
                "suggestions": f"<strong>Error generating suggestions:</strong><br>{str(e)}"
            }
    
    def generate_wellbeing_report(self, days: int = 7) -> Dict:
        """Generate wellbeing trend report from recent reflections"""
        
        if not self.reflections_history:
            return {
                "period": f"Last {days} days",
                "total_reflections": 0,
                "trend": "No data available",
                "recommendations": ["Start logging daily reflections to track wellbeing"]
            }
        
        # Get recent reflections
        cutoff_date = datetime.now() - timedelta(days=days)
        recent = [
            r for r in self.reflections_history
            if datetime.fromisoformat(r['timestamp']) >= cutoff_date
        ]
        
        if not recent:
            return {
                "period": f"Last {days} days",
                "total_reflections": 0,
                "trend": "No recent data",
                "recommendations": []
            }
        
        # Calculate average sentiment
        avg_sentiment = sum(r['analysis'].get('sentiment_score', 0) for r in recent) / len(recent)
        stress_levels = [r['analysis'].get('stress_level', 'unknown') for r in recent]
        high_stress_count = stress_levels.count('high')
        
        # All concerns
        all_concerns = []
        for r in recent:
            all_concerns.extend(r['analysis'].get('concerns', []))
        
        trend = "Stable"
        if avg_sentiment > 0.3:
            trend = "Positive"
        elif avg_sentiment < -0.3:
            trend = "Concerning"
        
        if high_stress_count > len(recent) / 2:
            trend = "High Stress Detected"
        
        return {
            "period": f"Last {days} days",
            "total_reflections": len(recent),
            "average_sentiment": round(avg_sentiment, 2),
            "high_stress_days": high_stress_count,
            "trend": trend,
            "common_concerns": list(set(all_concerns))[:5],
            "recommendations": self._get_trend_recommendations(trend, avg_sentiment)
        }
    
    def _get_trend_recommendations(self, trend: str, avg_sentiment: float) -> List[str]:
        """Get recommendations based on wellbeing trend"""
        
        if trend == "Positive":
            return [
                "Keep up the great work!",
                "Share your positive strategies with peers",
                "Continue current self-care practices"
            ]
        elif trend == "High Stress Detected":
            return [
                "Consider taking short breaks throughout the day",
                "Reach out to peer support network",
                "Review workload and prioritize tasks",
                "Practice daily mindfulness or relaxation",
                "Consider speaking with a counselor if stress persists"
            ]
        elif trend == "Concerning":
            return [
                "Implement stress management techniques",
                "Connect with supportive colleagues",
                "Review and adjust work-life balance",
                "Consider professional support if needed"
            ]
        else:
            return [
                "Continue regular wellbeing check-ins",
                "Maintain healthy work habits",
                "Stay connected with peer support"
            ]


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("LLAMA_MODEL", "llama-3.3-70b-versatile")
    
    monitor = WellbeingMonitor(api_key, model)
    
    # Test reflection analysis
    reflection = "Today was challenging. I had to manage three classes back-to-back, and some students were disruptive. Feeling a bit overwhelmed and exhausted."
    
    analysis = monitor.analyze_sentiment(reflection)
    print("Sentiment Analysis:")
    print(json.dumps(analysis, indent=2))
    
    interventions = monitor.provide_micro_intervention(analysis)
    print("\nSuggested Interventions:")
    print(json.dumps(interventions, indent=2))
