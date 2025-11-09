"""
Teacher Assistant System - Main Streamlit Application
Integrates all 4 features with an interactive UI
"""

import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
from PIL import Image
import io

# Import all feature modules
from assessment_grading import AssessmentGradingAssistant
from content_recommender import ContentRecommender, SAMPLE_RESOURCES
from wellbeing_monitor import WellbeingMonitor
from scheduling_rewards import SchedulingRewardSystem

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Teacher Assistant System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .feature-card {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .metric-card {
        background-color: #e1f5ff;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeeba;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .intervention-card {
        background-color: #e7f3ff;
        border-left: 4px solid #4a90e2;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        font-size: 1rem;
        line-height: 1.8;
        color: #333;
    }
    .intervention-card ul {
        margin: 0.5rem 0;
        padding-left: 1.5rem;
    }
    .intervention-card li {
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.api_key = os.getenv("GROQ_API_KEY")
    st.session_state.gemini_api_key = os.getenv("GEMINI_API_KEY")
    st.session_state.model = os.getenv("LLAMA_MODEL", "llama-3.3-70b-versatile")
    st.session_state.current_user = "teacher_demo"
    st.session_state.current_student = "student_demo"

def initialize_systems():
    """Initialize all AI systems"""
    if not st.session_state.initialized:
        with st.spinner("Initializing AI systems..."):
            try:
                # Initialize all systems
                st.session_state.grading_assistant = AssessmentGradingAssistant(
                    st.session_state.api_key,
                    st.session_state.model,
                    st.session_state.gemini_api_key
                )
                
                st.session_state.content_recommender = ContentRecommender(
                    st.session_state.api_key,
                    st.session_state.model
                )
                # Load sample resources
                st.session_state.content_recommender.add_learning_resources(SAMPLE_RESOURCES)
                
                st.session_state.wellbeing_monitor = WellbeingMonitor(
                    st.session_state.api_key,
                    st.session_state.model
                )
                
                st.session_state.scheduling_system = SchedulingRewardSystem(
                    st.session_state.api_key,
                    model=st.session_state.model
                )
                
                st.session_state.initialized = True
                st.success("✅ All systems initialized successfully!")
            except Exception as e:
                st.error(f"❌ Error initializing systems: {str(e)}")
                st.info("Please check your .env file and ensure GROQ_API_KEY is set correctly.")

# Main App
def main():
    st.markdown('<div class="main-header">🎓 AI Teacher Assistant System</div>', unsafe_allow_html=True)
    st.markdown("**Enhance teaching efficiency, student engagement, and teacher well-being with AI**")
    
    # Initialize systems
    initialize_systems()
    
    if not st.session_state.initialized:
        st.warning("⚠️ Please check your API configuration in the .env file")
        return
    
    # Sidebar navigation
    st.sidebar.title("🧭 Navigation")
    feature = st.sidebar.radio(
        "Select Feature:",
        [
            "🏠 Dashboard",
            "📝 AI Assessment & Grading",
            "📚 Content Recommender & Q/A",
            "💚 Teacher Well-being Monitor",
            "📅 Scheduling & Rewards"
        ]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"**User:** {st.session_state.current_user}")
    st.sidebar.info(f"**Model:** {st.session_state.model}")
    
    # Route to features
    if feature == "🏠 Dashboard":
        show_dashboard()
    elif feature == "📝 AI Assessment & Grading":
        show_assessment_grading()
    elif feature == "📚 Content Recommender & Q/A":
        show_content_recommender()
    elif feature == "💚 Teacher Well-being Monitor":
        show_wellbeing_monitor()
    elif feature == "📅 Scheduling & Rewards":
        show_scheduling_rewards()

def show_dashboard():
    """Display system dashboard with project overview"""
    
    # Hero Section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; 
                border-radius: 1rem; 
                color: white; 
                text-align: center;
                margin-bottom: 2rem;">
        <h1 style="margin: 0; font-size: 2.5rem;">🎓 AI Teacher Assistant System</h1>
        <p style="font-size: 1.2rem; margin: 0.5rem 0 0 0;">
            Empowering Educators with AI-Driven Tools for Enhanced Teaching Efficiency & Student Success
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Overview
    st.markdown("## 🚀 About This Project")
    st.markdown("""
    <div class="feature-card">
        <p style="font-size: 1.1rem; line-height: 1.8;">
        This <strong>AI-powered Teacher Assistant System</strong> is a comprehensive hackathon MVP that revolutionizes 
        classroom management by integrating <strong>4 cutting-edge AI features</strong> into a unified platform. 
        Built with <strong>Groq's Llama 3.3 70B</strong> and <strong>Google Gemini Vision API</strong>, 
        this system addresses real challenges teachers face daily—from grading workload to mental well-being.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Features Showcase
    st.markdown("## ✨ Core Features & AI Capabilities")
    
    # Feature 1
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("""
        <div style="text-align: center; font-size: 4rem; padding: 1rem;">
            📝
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="intervention-card">
            <h3>1️⃣ AI Assessment & Grading</h3>
            <p><strong>🤖 AI Models:</strong> Gemini Vision API + Groq Llama 3.3 70B</p>
            <p><strong>🎯 What it does:</strong></p>
            <ul>
                <li><strong>Handwriting OCR:</strong> Extracts text from student homework images using Gemini Vision</li>
                <li><strong>Intelligent Grading:</strong> AI analyzes answers and provides detailed scores, feedback, strengths & improvements</li>
                <li><strong>Multiple Choice Analysis:</strong> Auto-grades MCQ tests with instant results</li>
                <li><strong>Self-Evaluation Hints:</strong> Helps students reflect without revealing answers</li>
            </ul>
            <p><strong>💡 Use Case:</strong> Upload a photo of handwritten homework → Get instant grading + personalized feedback</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature 2
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("""
        <div style="text-align: center; font-size: 4rem; padding: 1rem;">
            📚
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="intervention-card">
            <h3>2️⃣ RAG-Based Content Recommender & Q/A</h3>
            <p><strong>🤖 AI Models:</strong> Sentence Transformers (all-MiniLM-L6-v2) + Groq Llama 3.3 70B</p>
            <p><strong>🎯 What it does:</strong></p>
            <ul>
                <li><strong>Smart Resource Search:</strong> Vector embeddings find the most relevant learning materials</li>
                <li><strong>RAG Q/A System:</strong> Answers questions using retrieved context from educational resources</li>
                <li><strong>Personalized Recommendations:</strong> Suggests Khan Academy, YouTube videos, articles based on topic & student level</li>
                <li><strong>Clickable Links:</strong> Direct access to curated educational content</li>
            </ul>
            <p><strong>💡 Use Case:</strong> Student asks "Explain photosynthesis" → AI retrieves relevant resources + generates comprehensive answer</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature 3
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("""
        <div style="text-align: center; font-size: 4rem; padding: 1rem;">
            💚
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="intervention-card">
            <h3>3️⃣ Teacher Well-being Monitor</h3>
            <p><strong>🤖 AI Models:</strong> Groq Llama 3.3 70B (Sentiment Analysis + NLP)</p>
            <p><strong>🎯 What it does:</strong></p>
            <ul>
                <li><strong>Sentiment Analysis:</strong> AI analyzes daily reflections to track emotional well-being</li>
                <li><strong>Micro-Interventions:</strong> Provides personalized stress-relief suggestions (breathing exercises, positive affirmations)</li>
                <li><strong>Peer Support Hub:</strong> Suggests colleague connections based on concerns (classroom management, work-life balance)</li>
                <li><strong>Well-being Reports:</strong> 7-day emotional trend analysis with actionable insights</li>
            </ul>
            <p><strong>💡 Use Case:</strong> Teacher logs "Feeling overwhelmed with grading" → AI detects stress + suggests peer support + offers 2-min breathing exercise</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature 4
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("""
        <div style="text-align: center; font-size: 4rem; padding: 1rem;">
            🤖
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="intervention-card">
            <h3>4️⃣ AI-Powered Scheduling & Intelligent Rewards</h3>
            <p><strong>🤖 AI Models:</strong> Groq Llama 3.3 70B (Schedule Optimization + Personalization)</p>
            <p><strong>🎯 What it does:</strong></p>
            <ul>
                <li><strong>AI Schedule Analysis:</strong> Detects time conflicts, workload imbalances, and deadline clusters</li>
                <li><strong>Optimal Time Suggestions:</strong> AI recommends best class times based on cognitive science & existing schedule</li>
                <li><strong>Gamified Rewards:</strong> Points & badges system for students/teachers</li>
                <li><strong>AI Reward Coach:</strong> Personalized motivation based on activity patterns & performance</li>
            </ul>
            <p><strong>💡 Use Case:</strong> Adding new Math class → AI suggests "Tuesday 10 AM" to avoid back-to-back classes + balance workload</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tech Stack
    st.markdown("## 🛠️ Technology Stack")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>🤖 AI/ML</h4>
            <ul style="text-align: left; padding-left: 1.5rem;">
                <li>Groq API (Llama 3.3 70B)</li>
                <li>Google Gemini Vision</li>
                <li>Sentence Transformers</li>
                <li>RAG Architecture</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>💻 Framework</h4>
            <ul style="text-align: left; padding-left: 1.5rem;">
                <li>Streamlit (Web UI)</li>
                <li>Python 3.11</li>
                <li>PIL/OpenCV</li>
                <li>NumPy/Pandas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>💾 Data Storage</h4>
            <ul style="text-align: left; padding-left: 1.5rem;">
                <li>JSON (Persistent)</li>
                <li>Vector Embeddings</li>
                <li>Session State</li>
                <li>File System</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Start Guide
    st.markdown("## 🚦 Quick Start Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 For Teachers:</h4>
            <ol>
                <li><strong>Grade Homework:</strong> Upload student work → Get AI feedback</li>
                <li><strong>Find Resources:</strong> Search topics → Get curated materials</li>
                <li><strong>Track Well-being:</strong> Log daily reflections → Get support</li>
                <li><strong>Manage Schedule:</strong> Add classes → Let AI optimize</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🎓 For Students:</h4>
            <ol>
                <li><strong>Self-Evaluation:</strong> Check your work → Get hints</li>
                <li><strong>Ask Questions:</strong> Get AI-powered explanations</li>
                <li><strong>Earn Rewards:</strong> Complete assignments → Unlock badges</li>
                <li><strong>Track Progress:</strong> View leaderboard → Stay motivated</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # System Stats
    st.markdown("## 📊 System Capabilities")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <h2 style="margin: 0;">4</h2>
            <p style="margin: 0.5rem 0 0 0;">AI Features</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white;">
            <h2 style="margin: 0;">3</h2>
            <p style="margin: 0.5rem 0 0 0;">AI Models</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white;">
            <h2 style="margin: 0;">∞</h2>
            <p style="margin: 0.5rem 0 0 0;">Use Cases</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white;">
            <h2 style="margin: 0;">100%</h2>
            <p style="margin: 0.5rem 0 0 0;">AI-Powered</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Call to Action
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1.5rem; 
                border-radius: 0.5rem; 
                color: white; 
                text-align: center;">
        <h3 style="margin: 0 0 0.5rem 0;">🎉 Ready to Experience AI-Powered Teaching?</h3>
        <p style="margin: 0; font-size: 1.1rem;">
            Choose a feature from the sidebar to get started! Each tool is designed to save time, reduce stress, and enhance learning outcomes.
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_assessment_grading():
    """Feature 1: AI Assessment & Grading Assistant"""
    st.header("📝 AI Assessment & Grading Assistant")
    
    tab1, tab2, tab3 = st.tabs(["📄 Text Grading", "🖼️ Image Grading (OCR)", "🔍 Self-Evaluation"])
    
    with tab1:
        st.subheader("Grade Text-based Homework")
        
        col1, col2 = st.columns(2)
        
        with col1:
            subject = st.selectbox("Subject", ["Mathematics", "Science", "Biology", "Physics", "Chemistry", "English", "History"])
            max_score = st.number_input("Maximum Score", min_value=1, max_value=100, value=10)
        
        with col2:
            correct_answer = st.text_area("Correct Answer / Solution", height=150, 
                placeholder="Enter the model answer or solution...")
        
        student_answer = st.text_area("Student's Answer", height=150,
            placeholder="Enter student's written answer...")
        
        if st.button("🎯 Grade Answer", key="grade_text"):
            if student_answer and correct_answer:
                with st.spinner("Grading..."):
                    grading_assistant = st.session_state.grading_assistant
                    result = grading_assistant.grade_homework(
                        student_answer, correct_answer, subject, max_score
                    )
                    
                    # Display results
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Score", f"{result['score']}/{max_score}")
                    with col2:
                        st.metric("Percentage", f"{result.get('percentage', 0):.1f}%")
                    
                    st.markdown("### 📋 Detailed Feedback")
                    st.info(result.get('feedback', 'No feedback available'))
                    
                    if result.get('strengths'):
                        st.markdown("### ✅ Strengths")
                        for strength in result['strengths']:
                            st.markdown(f"- {strength}")
                    
                    if result.get('improvements'):
                        st.markdown("### 📈 Areas for Improvement")
                        for improvement in result['improvements']:
                            st.markdown(f"- {improvement}")
                    
                    if result.get('mistakes'):
                        st.markdown("### ⚠️ Common Mistakes")
                        for mistake in result['mistakes']:
                            st.markdown(f"- {mistake}")
            else:
                st.warning("Please provide both student answer and correct answer")
    
    with tab2:
        st.subheader("Grade Handwritten Homework (OCR)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            subject_ocr = st.selectbox("Subject", ["Mathematics", "Science", "Biology", "Physics", "Chemistry", "English", "History"], key="subject_ocr")
            max_score_ocr = st.number_input("Maximum Score", min_value=1, max_value=100, value=10, key="max_ocr")
        
        with col2:
            correct_answer_ocr = st.text_area("Correct Answer / Solution", height=100, key="correct_ocr",
                placeholder="Enter the model answer...")
        
        uploaded_file = st.file_uploader("Upload homework image (handwritten/printed)", 
                                        type=['png', 'jpg', 'jpeg'], key="upload_hw")
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Homework", use_column_width=True)
            
            if st.button("🔍 Extract Text & Grade", key="grade_ocr"):
                if correct_answer_ocr:
                    with st.spinner("Extracting text using OCR..."):
                        import tempfile
                        import uuid
                        
                        # Create a unique temporary file
                        temp_filename = f"temp_homework_{uuid.uuid4().hex[:8]}.png"
                        temp_path = os.path.join(tempfile.gettempdir(), temp_filename)
                        
                        try:
                            # Save uploaded file temporarily
                            image.save(temp_path)
                            
                            grading_assistant = st.session_state.grading_assistant
                            result = grading_assistant.grade_from_image(
                                temp_path, correct_answer_ocr, subject_ocr, max_score_ocr
                            )
                        finally:
                            # Clean up - ensure file is closed before deletion
                            try:
                                if os.path.exists(temp_path):
                                    import time
                                    time.sleep(0.1)  # Brief delay to ensure file is released
                                    os.remove(temp_path)
                            except (PermissionError, FileNotFoundError):
                                pass  # File will be cleaned up by OS temp cleanup
                        
                        # Display extracted text
                        st.markdown("### 📄 Extracted Text")
                        st.text_area("OCR Result", result.get('extracted_text', ''), height=100, key="extracted")
                        
                        # Display results
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Score", f"{result['score']}/{max_score_ocr}")
                        with col2:
                            st.metric("Percentage", f"{result.get('percentage', 0):.1f}%")
                        
                        st.markdown("### 📋 Feedback")
                        st.info(result.get('feedback', 'No feedback available'))
                else:
                    st.warning("Please provide the correct answer")
    
    with tab3:
        st.subheader("Student Self-Evaluation")
        st.info("Students can scan their homework to get hints and self-check before submission")
        
        subject_self = st.selectbox("Subject", ["Mathematics", "Science", "Biology", "Physics", "Chemistry", "English", "History"], key="subject_self")
        
        student_ans_self = st.text_area("Your Answer", height=150, key="self_ans",
            placeholder="Enter your answer to get self-evaluation hints...")
        
        if st.button("💡 Get Hints", key="get_hints"):
            if student_ans_self:
                with st.spinner("Generating hints..."):
                    grading_assistant = st.session_state.grading_assistant
                    hints = grading_assistant.provide_self_evaluation_hints(
                        student_ans_self, subject_self
                    )
                    
                    st.markdown("### 📊 Estimated Score Range")
                    st.success(hints.get('estimated_score_range', 'N/A'))
                    
                    if hints.get('hints'):
                        st.markdown("### 💡 Hints for Improvement")
                        for hint in hints['hints']:
                            st.markdown(f"- {hint}")
                    
                    if hints.get('review_topics'):
                        st.markdown("### 📚 Topics to Review")
                        for topic in hints['review_topics']:
                            st.markdown(f"- {topic}")
                    
                    if hints.get('reflection_questions'):
                        st.markdown("### 🤔 Self-Reflection Questions")
                        for question in hints['reflection_questions']:
                            st.markdown(f"- {question}")
            else:
                st.warning("Please enter your answer")

def show_content_recommender():
    """Feature 2: Personalized Content Recommender & Q/A"""
    st.header("📚 Personalized Content Recommender & Q/A Agent")
    
    tab1, tab2, tab3 = st.tabs(["🎯 Content Recommendations", "❓ Q&A Agent", "📄 Generate Worksheet"])
    
    with tab1:
        st.subheader("Get Personalized Learning Resources")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            topic = st.text_input("Topic", placeholder="e.g., Photosynthesis, Algebra, etc.")
        
        with col2:
            student_level = st.selectbox("Student Level", ["beginner", "intermediate", "advanced"])
        
        with col3:
            teaching_method = st.selectbox("Teaching Method", ["Any", "visual", "interactive", "discussion"])
        
        num_recs = st.slider("Number of Recommendations", 1, 5, 3)
        
        if st.button("🔍 Find Resources", key="find_resources"):
            if topic:
                with st.spinner("Finding best resources..."):
                    recommender = st.session_state.content_recommender
                    method = None if teaching_method == "Any" else teaching_method
                    result = recommender.recommend_content(
                        topic, student_level, method, num_recs
                    )
                    
                    st.markdown("### 📚 Recommended Resources")
                    
                    for i, resource in enumerate(result['recommendations'], 1):
                        url = resource.get('url', '#')
                        st.markdown(f"""
                        <div class="feature-card">
                            <strong>{i}. {resource['topic']}</strong><br>
                            <em>{resource['resource_type'].title()} | {resource['difficulty'].title()}</em><br>
                            <small>Teaching Method: {resource['teaching_method']}</small><br><br>
                            {resource['content']}<br><br>
                            <small>Relevance Score: {resource['similarity_score']:.2%}</small><br>
                            {'<a href="' + url + '" target="_blank" style="color: #1f77b4; text-decoration: none;">🔗 Access Resource →</a>' if url != '#' else ''}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("### 🎯 Why These Resources?")
                    st.info(result['explanation'])
            else:
                st.warning("Please enter a topic")
    
    with tab2:
        st.subheader("Ask Subject-Related Questions")
        
        context_topic = st.text_input("Context Topic (optional)", placeholder="e.g., Biology, Physics...")
        question = st.text_area("Your Question", height=100, 
            placeholder="Ask any subject-related question...")
        
        if st.button("💬 Get Answer", key="get_answer"):
            if question:
                with st.spinner("Thinking..."):
                    recommender = st.session_state.content_recommender
                    answer_result = recommender.answer_question(question, context_topic)
                    
                    st.markdown("### 📝 Answer")
                    st.markdown(f'<div class="success-box">{answer_result["answer"]}</div>', 
                               unsafe_allow_html=True)
                    
                    if answer_result['sources']:
                        st.markdown("### 📚 Sources Referenced")
                        for source in answer_result['sources']:
                            st.markdown(f"- {source}")
                    
                    confidence_color = {"high": "green", "medium": "orange", "low": "red", "none": "gray"}
                    st.markdown(f"**Confidence:** :{confidence_color.get(answer_result['confidence'], 'gray')}[{answer_result['confidence'].upper()}]")
            else:
                st.warning("Please enter a question")
    
    with tab3:
        st.subheader("Generate Practice Worksheet")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            worksheet_topic = st.text_input("Worksheet Topic", placeholder="e.g., Algebra, Cell Biology...")
        
        with col2:
            worksheet_difficulty = st.selectbox("Difficulty", ["beginner", "intermediate", "advanced"], key="ws_diff")
        
        with col3:
            num_questions = st.slider("Number of Questions", 3, 10, 5)
        
        if st.button("📄 Generate Worksheet", key="gen_worksheet"):
            if worksheet_topic:
                with st.spinner("Creating worksheet..."):
                    recommender = st.session_state.content_recommender
                    worksheet = recommender.generate_practice_worksheet(
                        worksheet_topic, worksheet_difficulty, num_questions
                    )
                    
                    st.markdown(f"## {worksheet['title']}")
                    st.markdown("---")
                    
                    for i, q in enumerate(worksheet['questions'], 1):
                        st.markdown(f"### Question {i} ({q['type'].upper()})")
                        st.markdown(f"**{q['question']}**")
                        
                        with st.expander("Show Answer"):
                            st.success(f"**Answer:** {q['answer']}")
                            if q.get('explanation'):
                                st.info(f"**Explanation:** {q['explanation']}")
                        
                        st.markdown("---")
            else:
                st.warning("Please enter a topic")

def show_wellbeing_monitor():
    """Feature 3: Teacher Well-being Monitor"""
    st.header("💚 Teacher Well-being Monitor & Peer Support")
    
    tab1, tab2, tab3 = st.tabs(["📝 Daily Reflection", "📊 Wellbeing Report", "🤝 Peer Support"])
    
    with tab1:
        st.subheader("Log Your Daily Reflection")
        
        reflection = st.text_area("How are you feeling today? Share your thoughts...", 
                                 height=150, 
                                 placeholder="Reflect on your day, challenges, achievements...")
        
        if st.button("💭 Analyze Reflection", key="analyze_reflection"):
            if reflection:
                with st.spinner("Analyzing your wellbeing..."):
                    monitor = st.session_state.wellbeing_monitor
                    analysis = monitor.analyze_sentiment(reflection)
                    
                    # Display sentiment score
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        sentiment = analysis['sentiment_score']
                        sentiment_emoji = "😊" if sentiment > 0.3 else "😐" if sentiment > -0.3 else "😔"
                        st.metric("Sentiment", f"{sentiment_emoji} {sentiment:.2f}", 
                                 help="-1 (negative) to +1 (positive)")
                    
                    with col2:
                        stress_level = analysis['stress_level']
                        stress_color = {"low": "green", "medium": "orange", "high": "red"}
                        st.metric("Stress Level", stress_level.upper())
                    
                    with col3:
                        st.metric("Emotions Detected", len(analysis.get('emotions', [])))
                    
                    st.markdown("### 🧠 Analysis Summary")
                    st.info(analysis.get('overall_assessment', 'No assessment available'))
                    
                    if analysis.get('emotions'):
                        st.markdown("### 🎭 Emotions Detected")
                        emotions_str = ", ".join(analysis['emotions'])
                        st.write(emotions_str)
                    
                    if analysis.get('concerns'):
                        st.markdown("### ⚠️ Concerns")
                        for concern in analysis['concerns']:
                            st.markdown(f"- {concern}")
                    
                    if analysis.get('positive_aspects'):
                        st.markdown("### ✨ Positive Aspects")
                        for positive in analysis['positive_aspects']:
                            st.markdown(f"- {positive}")
                    
                    # Get interventions
                    st.markdown("---")
                    st.markdown("## 🎯 Suggested Interventions")
                    
                    interventions = monitor.provide_micro_intervention(analysis)
                    
                    priority = interventions.get('priority', 'medium')
                    priority_color = {"low": "green", "medium": "orange", "high": "red"}
                    st.markdown(f"**Priority Level:** :{priority_color[priority]}[{priority.upper()}]")
                    
                    for intervention in interventions.get('interventions', []):
                        st.markdown(f"""
                        <div class="intervention-card">
                            <strong>🎯 {intervention['title']}</strong> <span style="color: #666;">({intervention['duration']})</span><br><br>
                            {intervention['description']}<br><br>
                            <em style="color: #2e7d32;">✅ Benefit: {intervention['benefit']}</em>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if interventions.get('seek_support'):
                        st.warning(f"🤝 {interventions.get('support_message', 'Consider reaching out for support')}")
            else:
                st.warning("Please write a reflection")
    
    with tab2:
        st.subheader("Your Wellbeing Trends")
        
        days = st.slider("View last N days", 7, 30, 7, key="wellbeing_days")
        
        if st.button("📈 Generate Report", key="gen_wellbeing_report"):
            monitor = st.session_state.wellbeing_monitor
            report = monitor.generate_wellbeing_report(days)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Reflections", report['total_reflections'])
            
            with col2:
                avg_sent = report.get('average_sentiment', 0)
                st.metric("Avg Sentiment", f"{avg_sent:.2f}")
            
            with col3:
                st.metric("High Stress Days", report.get('high_stress_days', 0))
            
            st.markdown(f"### 📊 Overall Trend: {report['trend']}")
            
            if report.get('common_concerns'):
                st.markdown("### 🔍 Common Concerns")
                for concern in report['common_concerns']:
                    st.markdown(f"- {concern}")
            
            if report.get('recommendations'):
                st.markdown("### 💡 Recommendations")
                for rec in report['recommendations']:
                    st.markdown(f"- {rec}")
    
    with tab3:
        st.subheader("Peer Support Hub")
        
        concern_type = st.selectbox(
            "What kind of support do you need?",
            ["Classroom Management", "Work-Life Balance", "Student Engagement", 
             "Curriculum Planning", "Technology Integration", "General Support"]
        )
        
        if st.button("🤝 Get Peer Support Suggestions", key="peer_support"):
            with st.spinner("Finding support options..."):
                monitor = st.session_state.wellbeing_monitor
                support = monitor.get_peer_support_suggestions(concern_type)
                
                st.markdown(f"### 🤝 Support for: {support['concern_type']}")
                
                # Display suggestions in a styled container
                suggestions_html = f"""
                <div class="intervention-card">
                    {support['suggestions']}
                </div>
                """
                st.markdown(suggestions_html, unsafe_allow_html=True)

def show_scheduling_rewards():
    """Feature 4: AI-Powered Scheduling & Intelligent Rewards"""
    st.header("🤖 AI-Powered Scheduling & Intelligent Rewards")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📅 Schedule", "🤖 AI Schedule Assistant", "➕ Add Events", "🏆 Rewards", "📊 Leaderboard"])
    
    with tab1:
        st.subheader("Your Schedule")
        
        schedule_sys = st.session_state.scheduling_system
        
        # Refresh button to reload schedule
        if st.button("🔄 Refresh Schedule", key="refresh_schedule"):
            st.session_state.scheduling_system.schedule = st.session_state.scheduling_system._load_schedule()
            st.success("Schedule refreshed!")
            st.rerun()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📚 Today's Classes")
            todays_classes = schedule_sys.get_todays_classes()
            
            if todays_classes:
                for cls in todays_classes:
                    st.markdown(f"""
                    <div class="feature-card">
                        <strong>{cls['name']}</strong><br>
                        📖 Subject: {cls['subject']}<br>
                        🕐 {cls['start_time']} - {cls['end_time']}<br>
                        📍 {cls.get('room', 'N/A')}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No classes today")
            
            # Show all classes
            st.markdown("### 📅 All Scheduled Classes")
            all_classes = schedule_sys.schedule['classes']
            if all_classes:
                for cls in all_classes:
                    st.markdown(f"- **{cls['day']}** {cls['start_time']}-{cls['end_time']}: {cls['name']} ({cls['subject']})")
            else:
                st.info("No classes scheduled yet")
        
        with col2:
            st.markdown("### 📋 Upcoming Assignments")
            days = st.slider("Show next N days", 1, 30, 7, key="upcoming_days")
            upcoming = schedule_sys.get_upcoming_schedule(days)
            
            if upcoming['assignments']:
                for assign in upcoming['assignments']:
                    days_until = assign.get('days_until_due', 0)
                    urgency = "🔴" if days_until <= 1 else "🟡" if days_until <= 3 else "🟢"
                    
                    st.markdown(f"""
                    <div class="feature-card">
                        {urgency} <strong>{assign['title']}</strong><br>
                        📖 {assign['subject']}<br>
                        📅 Due: {assign['due_date']}<br>
                        ⏰ {days_until} days remaining<br>
                        🎯 Points: {assign.get('points', 10)}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info(f"No assignments in the next {days} days")
    
    with tab2:
        st.subheader("🤖 AI Schedule Assistant")
        
        st.markdown("### 🔍 AI Schedule Analysis")
        st.info("Let AI analyze your schedule for conflicts, workload balance, and optimization opportunities!")
        
        if st.button("🧠 Analyze My Schedule", key="analyze_schedule"):
            with st.spinner("AI is analyzing your schedule..."):
                schedule_sys = st.session_state.scheduling_system
                analysis = schedule_sys.ai_analyze_schedule_conflicts()
                
                if analysis['status'] == 'success':
                    st.markdown(f"""
                    <div class="intervention-card">
                        <h4>📊 AI Schedule Analysis</h4>
                        <p><strong>Total Classes:</strong> {analysis['total_classes']}</p>
                        <p><strong>Pending Assignments:</strong> {analysis['pending_assignments']}</p>
                        <hr>
                        {analysis['analysis']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"Analysis failed: {analysis.get('analysis', 'Unknown error')}")
        
        st.markdown("---")
        st.markdown("### 💡 AI Optimal Time Suggestion")
        st.info("Planning a new class? Ask AI to suggest the best time slot!")
        
        col1, col2 = st.columns(2)
        with col1:
            suggest_subject = st.selectbox("Subject to schedule", 
                ["Mathematics", "Science", "Biology", "Physics", "Chemistry", "English", "History", "Computer Science"],
                key="suggest_subject")
        with col2:
            suggest_duration = st.number_input("Duration (minutes)", 30, 180, 60, step=15, key="suggest_duration")
        
        if st.button("🎯 Get AI Time Suggestion", key="ai_time_suggest"):
            with st.spinner("AI is finding the optimal time slot..."):
                schedule_sys = st.session_state.scheduling_system
                suggestion = schedule_sys.ai_suggest_optimal_time(suggest_subject, suggest_duration)
                
                if suggestion['status'] == 'success':
                    st.markdown(f"""
                    <div class="intervention-card">
                        <h4>💡 AI Recommendation for {suggest_subject}</h4>
                        {suggestion['suggestion']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"Suggestion failed: {suggestion.get('suggestion', 'Unknown error')}")
    
    with tab3:
        st.subheader("Add New Events")
        
        event_type = st.radio("Event Type", ["Class", "Assignment"])
        
        if event_type == "Class":
            st.markdown("### Add New Class")
            
            class_name = st.text_input("Class Name", placeholder="e.g., Mathematics 101")
            subject = st.selectbox("Subject", ["Mathematics", "Science", "Biology", "Physics", "Chemistry", "English", "History", "Computer Science"])
            
            col1, col2 = st.columns(2)
            with col1:
                day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
                start_time = st.time_input("Start Time")
            
            with col2:
                room = st.text_input("Room", placeholder="e.g., Room 101")
                end_time = st.time_input("End Time")
            
            if st.button("➕ Add Class", key="add_class"):
                if class_name:
                    schedule_sys = st.session_state.scheduling_system
                    class_id = schedule_sys.add_class({
                        "name": class_name,
                        "day": day,
                        "start_time": start_time.strftime("%H:%M"),
                        "end_time": end_time.strftime("%H:%M"),
                        "subject": subject,
                        "room": room
                    })
                    st.success(f"✅ Class added successfully! ID: {class_id}")
                    st.info("💡 Go to 'Schedule' tab and click 'Refresh Schedule' to see your new class!")
                else:
                    st.warning("Please provide class name")
        
        else:  # Assignment
            st.markdown("### Add New Assignment")
            
            assign_title = st.text_input("Assignment Title", placeholder="e.g., Homework Chapter 5")
            assign_subject = st.selectbox("Subject", ["Mathematics", "Science", "Biology", "Physics", "Chemistry", "English", "History", "Computer Science"], key="assign_subject")
            
            col1, col2 = st.columns(2)
            with col1:
                due_date = st.date_input("Due Date")
            with col2:
                points = st.number_input("Points", min_value=1, max_value=100, value=10)
            
            description = st.text_area("Description (optional)", placeholder="Assignment details...")
            
            if st.button("➕ Add Assignment", key="add_assign"):
                if assign_title:
                    schedule_sys = st.session_state.scheduling_system
                    assign_id = schedule_sys.add_assignment({
                        "title": assign_title,
                        "subject": assign_subject,
                        "due_date": due_date.isoformat(),
                        "description": description,
                        "points": points
                    })
                    st.success(f"✅ Assignment added successfully! ID: {assign_id}")
                    st.info("💡 Go to 'Schedule' tab and click 'Refresh Schedule' to see your new assignment!")
                else:
                    st.warning("Please provide assignment title")
    
    with tab4:
        st.subheader("🏆 Your Rewards")
        
        # User ID management
        st.markdown("### 👤 User ID Management")
        user_type = st.radio("Select user type:", ["Teacher", "Student"])
        
        col1, col2 = st.columns([3, 1])
        with col1:
            if user_type == "Teacher":
                user_id = st.text_input("Teacher ID", value=st.session_state.current_user, key="teacher_id_input")
                if st.button("Set Teacher ID", key="set_teacher_id"):
                    st.session_state.current_user = user_id
                    st.success(f"Teacher ID set to: {user_id}")
            else:
                user_id = st.text_input("Student ID", value=st.session_state.current_student, key="student_id_input")
                if st.button("Set Student ID", key="set_student_id"):
                    st.session_state.current_student = user_id
                    st.success(f"Student ID set to: {user_id}")
        
        with col2:
            st.info(f"Current {user_type} ID:\n**{user_id}**")
        
        st.markdown("---")
        
        schedule_sys = st.session_state.scheduling_system
        profile = schedule_sys.get_user_profile(user_id, user_type.lower())
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Points", profile.get('total_points', 0))
        
        with col2:
            st.metric("Badges Earned", profile.get('badge_count', 0))
        
        with col3:
            rank = profile.get('rank', 'N/A')
            st.metric("Rank", f"#{rank}" if rank else "Unranked")
        
        # AI Personalized Recommendations
        st.markdown("### 🤖 AI Personalized Recommendations")
        if st.button("🧠 Get AI Reward Suggestions", key="ai_rewards"):
            with st.spinner("AI is analyzing your performance..."):
                recommendations = schedule_sys.ai_personalized_reward_suggestions(user_id, user_type.lower())
                
                if recommendations['status'] == 'success':
                    st.markdown(f"""
                    <div class="intervention-card">
                        <h4>💡 Personalized Motivation for {user_id}</h4>
                        {recommendations['recommendations']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"Recommendations failed: {recommendations.get('recommendations', 'Unknown error')}")
        
        if profile.get('badges'):
            st.markdown("### 🎖️ Your Badges")
            
            cols = st.columns(3)
            for i, badge in enumerate(profile['badges']):
                with cols[i % 3]:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div style="font-size: 3rem;">{badge.get('icon', '🏅')}</div>
                        <strong>{badge['name']}</strong><br>
                        <small>{badge['description']}</small>
                    </div>
                    """, unsafe_allow_html=True)
        
        if profile.get('recent_activity'):
            st.markdown("### 📊 Recent Activity")
            for activity in profile['recent_activity']:
                st.markdown(f"- **+{activity['points']} points** - {activity['reason']} ({activity['timestamp'][:10]})")
        
        # Add points manually (for demo)
        st.markdown("---")
        st.markdown("### ➕ Add Points (Demo)")
        
        col1, col2 = st.columns(2)
        with col1:
            demo_points = st.number_input("Points to add", 1, 100, 10, key="demo_points")
        with col2:
            demo_reason = st.text_input("Reason", "Test points", key="demo_reason")
        
        if st.button("Add Points", key="add_demo_points"):
            result = schedule_sys.add_points(user_id, demo_points, user_type.lower(), demo_reason)
            st.success(f"✅ Added {demo_points} points! Total: {result['total_points']}")
            
            if result.get('new_badges'):
                st.balloons()
                st.success(f"🎉 New badge(s) earned: {', '.join([b['name'] for b in result['new_badges']])}")
    
    with tab5:
        st.subheader("📊 Leaderboard")
        
        leaderboard_type = st.radio("Show leaderboard for:", ["Students", "Teachers"], key="leaderboard_type")
        top_n = st.slider("Show top N users", 5, 20, 10)
        
        schedule_sys = st.session_state.scheduling_system
        leaderboard = schedule_sys.get_leaderboard(leaderboard_type.lower()[:-1], top_n)
        
        if leaderboard:
            st.markdown("### 🏆 Top Performers")
            
            for i, user in enumerate(leaderboard, 1):
                medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
                
                st.markdown(f"""
                <div class="feature-card">
                    <strong>{medal} {user['name']}</strong><br>
                    🎯 Points: {user['total_points']} | 🎖️ Badges: {user['badge_count']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No data available yet")

if __name__ == "__main__":
    main()
