# 🎓 AI Teacher Assistant System

A comprehensive Teacher Assistant System that enhances teaching efficiency, student engagement, and teacher well-being using AI and automation.

## 🌟 Features

### 1. 📝 AI Assessment & Grading Assistant
- Automatically evaluate text-based and handwritten homework
- OCR support using EasyOCR for reading scanned pages
- Instant feedback with strengths and improvement areas
- Student self-evaluation with hints (no spoilers!)

### 2. 📚 Personalized Content Recommender & Q/A Agent
- RAG-powered recommendations using vector embeddings
- Smart Q&A agent for subject-related questions
- Generate practice worksheets automatically
- Personalized by student level and teaching methodology

### 3. 💚 Teacher Well-being Monitor
- Daily reflection analysis with sentiment detection
- Stress level monitoring using AI
- Personalized micro-interventions
- Peer support suggestions
- Wellbeing trend reports

### 4. 📅 Scheduling, Notifications & Reward System
- Timetable management for classes
- Assignment tracking with reminders
- Gamification with points and badges
- Leaderboard for motivation
- JSON-based persistent storage

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key (get from https://console.groq.com/)
- Tesseract OCR (for handwriting recognition)

### Installation

1. **Clone/Download the project**
   ```bash
   cd "d:\Documents\UNI\3rd  Year\Application of Ai\Project"
   ```

2. **Install Tesseract OCR** (for Windows)
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install to default location (C:\Program Files\Tesseract-OCR)
   - Add to PATH environment variable

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**
   - Your API key is already set in `.env` file
   - Model: `llama-3.3-70b-versatile`

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser**
   - The app will automatically open at `http://localhost:8501`

## 📁 Project Structure

```
Project/
├── app.py                      # Main Streamlit application
├── assessment_grading.py       # Feature 1: AI Grading
├── content_recommender.py      # Feature 2: Content & Q/A
├── wellbeing_monitor.py        # Feature 3: Wellbeing
├── scheduling_rewards.py       # Feature 4: Scheduling & Rewards
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── data/                       # Data storage (auto-created)
    ├── schedule.json
    └── rewards.json
```

## 🎯 Usage Guide

### Dashboard
- Overview of all metrics
- Today's schedule
- Upcoming assignments
- Quick actions

### AI Assessment & Grading
1. **Text Grading**: Enter student answer and model answer
2. **Image Grading**: Upload handwritten homework for OCR + grading
3. **Self-Evaluation**: Students get hints without answers

### Content Recommender
1. **Find Resources**: Search by topic, level, teaching method
2. **Q&A Agent**: Ask subject questions with context
3. **Worksheets**: Generate practice questions automatically

### Well-being Monitor
1. **Daily Reflection**: Log feelings and get analysis
2. **View Reports**: Track wellbeing trends over time
3. **Peer Support**: Get suggestions for connecting with colleagues

### Scheduling & Rewards
1. **View Schedule**: See classes and assignments
2. **Add Events**: Create new classes or assignments
3. **Rewards**: Track points and badges
4. **Leaderboard**: See top performers

## 🔧 Configuration

### Environment Variables (.env)
```
GROQ_API_KEY=your_api_key_here
LLAMA_MODEL=llama-3.3-70b-versatile
DEBUG=True
MAX_FILE_SIZE=10485760
```

### Adding Learning Resources
Edit `content_recommender.py` and add to `SAMPLE_RESOURCES`:
```python
{
    "topic": "Your Topic",
    "content": "Description of the resource...",
    "resource_type": "video/article/worksheet",
    "difficulty": "beginner/intermediate/advanced",
    "teaching_method": "visual/interactive/discussion"
}
```

### Customizing Badges
Edit `scheduling_rewards.py` in `_get_default_badges()` method.

## 🎨 Technologies Used

- **Frontend**: Streamlit
- **AI Model**: Groq (Llama 3.3-70b-versatile)
- **OCR**: EasyOCR / Pytesseract
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Storage**: JSON files
- **Image Processing**: Pillow, OpenCV

## 📊 Demo Data

The system includes sample data for testing:
- 5 learning resources across different subjects
- Badge system with 6 different achievements
- Default teacher and student profiles

## 🐛 Troubleshooting

### OCR Not Working
- Ensure Tesseract is installed and in PATH
- For EasyOCR: First run will download models (~100MB)

### API Errors
- Check your Groq API key in `.env`
- Verify you have API credits
- Check internet connection

### Import Errors
- Run: `pip install -r requirements.txt`
- Make sure you're using Python 3.8+

### Streamlit Issues
- Clear cache: `streamlit cache clear`
- Restart the app

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Deploy to Streamlit Cloud
1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Add secrets (API keys) in settings
4. Deploy!

### Deploy to Lovable.dev
1. Create new project on lovable.dev
2. Upload all Python files
3. Configure environment variables
4. Launch application

## 📝 Notes

- First OCR operation will download models (1-2 minutes)
- Embedding model downloads on first use (~80MB)
- All data stored in `data/` folder (JSON files)
- Images processed temporarily and deleted

## 🤝 Contributing

This is a hackathon MVP. Feel free to extend with:
- Database integration (PostgreSQL, MongoDB)
- Email notifications
- Mobile app version
- Advanced analytics
- Multi-language support

## 📄 License

MIT License - Free for educational and commercial use

## 👥 Authors

Built for AI Application Course Project - 3rd Year

## 🙏 Acknowledgments

- Groq for fast LLM inference
- EasyOCR for handwriting recognition
- Streamlit for rapid UI development
- Sentence Transformers for embeddings

---

**Ready to revolutionize teaching with AI!** 🎓✨
