"""
Test script to verify all components are working
"""

import os
from dotenv import load_dotenv

def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    
    try:
        import streamlit
        print("✓ Streamlit")
    except ImportError:
        print("✗ Streamlit - Run: pip install streamlit")
    
    try:
        from groq import Groq
        print("✓ Groq")
    except ImportError:
        print("✗ Groq - Run: pip install groq")
    
    try:
        from PIL import Image
        print("✓ Pillow")
    except ImportError:
        print("✗ Pillow - Run: pip install pillow")
    
    try:
        import easyocr
        print("✓ EasyOCR")
    except ImportError:
        print("✗ EasyOCR - Run: pip install easyocr")
    
    try:
        from sentence_transformers import SentenceTransformer
        print("✓ Sentence Transformers")
    except ImportError:
        print("✗ Sentence Transformers - Run: pip install sentence-transformers")
    
    print()

def test_environment():
    """Test environment variables"""
    print("Testing environment...")
    
    load_dotenv()
    
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("LLAMA_MODEL")
    
    if api_key:
        print(f"✓ GROQ_API_KEY found (length: {len(api_key)})")
    else:
        print("✗ GROQ_API_KEY not found in .env")
    
    if model:
        print(f"✓ LLAMA_MODEL: {model}")
    else:
        print("✗ LLAMA_MODEL not set")
    
    print()

def test_groq_connection():
    """Test Groq API connection"""
    print("Testing Groq API connection...")
    
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("LLAMA_MODEL", "llama-3.3-70b-versatile")
    
    if not api_key:
        print("✗ Cannot test - API key not found")
        return
    
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": "Say 'Hello' in one word"}
            ],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"✓ Groq API working! Response: {result}")
    except Exception as e:
        print(f"✗ Groq API error: {str(e)}")
    
    print()

def test_modules():
    """Test if all feature modules can be imported"""
    print("Testing feature modules...")
    
    try:
        from assessment_grading import AssessmentGradingAssistant
        print("✓ assessment_grading.py")
    except ImportError as e:
        print(f"✗ assessment_grading.py - {str(e)}")
    
    try:
        from content_recommender import ContentRecommender
        print("✓ content_recommender.py")
    except ImportError as e:
        print(f"✗ content_recommender.py - {str(e)}")
    
    try:
        from wellbeing_monitor import WellbeingMonitor
        print("✓ wellbeing_monitor.py")
    except ImportError as e:
        print(f"✗ wellbeing_monitor.py - {str(e)}")
    
    try:
        from scheduling_rewards import SchedulingRewardSystem
        print("✓ scheduling_rewards.py")
    except ImportError as e:
        print(f"✗ scheduling_rewards.py - {str(e)}")
    
    print()

def main():
    print("=" * 50)
    print("AI TEACHER ASSISTANT SYSTEM - TEST")
    print("=" * 50)
    print()
    
    test_imports()
    test_environment()
    test_modules()
    test_groq_connection()
    
    print("=" * 50)
    print("Testing complete!")
    print("=" * 50)
    print()
    print("If all tests passed, run: streamlit run app.py")
    print()

if __name__ == "__main__":
    main()
