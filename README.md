# 🎓 AI-Powered Productivity Engine for Teachers# 🎓 AI Teacher Assistant System



> A comprehensive AI-powered platform that enhances teaching efficiency, student engagement, and teacher well-being through automation and intelligent features.A comprehensive Teacher Assistant System that enhances teaching efficiency, student engagement, and teacher well-being using AI and automation.



[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)## 🌟 Features

[![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)](https://streamlit.io/)

[![Groq](https://img.shields.io/badge/Groq-Llama--3.3-green.svg)](https://groq.com/)### 1. 📝 AI Assessment & Grading Assistant

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)- Automatically evaluate text-based and handwritten homework

- OCR support using EasyOCR for reading scanned pages

## 🌟 Overview- Instant feedback with strengths and improvement areas

- Student self-evaluation with hints (no spoilers!)

This AI Teacher Assistant System is a hackathon MVP that revolutionizes classroom management by reducing manual workload, promoting smarter teaching practices, and making education more personalized and supportive. Built with cutting-edge AI models including **Groq's Llama 3.3 70B** and **Google Gemini Vision API**.

### 2. 📚 Personalized Content Recommender & Q/A Agent

## ✨ Features- RAG-powered recommendations using vector embeddings

- Smart Q&A agent for subject-related questions

### 1️⃣ AI Assessment & Grading Assistant- Generate practice worksheets automatically

**🤖 Tech:** Gemini Vision API + Groq Llama 3.3 70B- Personalized by student level and teaching methodology



- 📝 **Handwriting OCR**: Extract text from student homework images using Gemini Vision### 3. 💚 Teacher Well-being Monitor

- 🎯 **Intelligent Grading**: AI analyzes answers and provides detailed scores, feedback, strengths & improvements- Daily reflection analysis with sentiment detection

- ✅ **Multiple Choice Analysis**: Auto-grades MCQ tests with instant results- Stress level monitoring using AI

- 💡 **Self-Evaluation Hints**: Helps students reflect without revealing answers- Personalized micro-interventions

- Peer support suggestions

**Use Case**: Upload a photo of handwritten homework → Get instant grading + personalized feedback- Wellbeing trend reports



### 2️⃣ RAG-Based Content Recommender & Q/A### 4. 📅 Scheduling, Notifications & Reward System

**🤖 Tech:** Sentence Transformers (all-MiniLM-L6-v2) + Groq Llama 3.3 70B- Timetable management for classes

- Assignment tracking with reminders

- 🔍 **Smart Resource Search**: Vector embeddings find the most relevant learning materials- Gamification with points and badges

- 💬 **RAG Q/A System**: Answers questions using retrieved context from educational resources- Leaderboard for motivation

- 📚 **Personalized Recommendations**: Suggests Khan Academy, YouTube videos, articles based on topic & student level- JSON-based persistent storage

- 🔗 **Clickable Links**: Direct access to curated educational content

## 🚀 Quick Start

**Use Case**: Student asks "Explain photosynthesis" → AI retrieves relevant resources + generates comprehensive answer

### Prerequisites

### 3️⃣ Teacher Well-being Monitor- Python 3.8 or higher

**🤖 Tech:** Groq Llama 3.3 70B (Sentiment Analysis + NLP)- Groq API key (get from https://console.groq.com/)

- Tesseract OCR (for handwriting recognition)

- 💚 **Sentiment Analysis**: AI analyzes daily reflections to track emotional well-being

- 🎯 **Micro-Interventions**: Provides personalized stress-relief suggestions (breathing exercises, positive affirmations)### Installation

- 🤝 **Peer Support Hub**: Suggests colleague connections based on concerns

- 📊 **Well-being Reports**: 7-day emotional trend analysis with actionable insights1. **Clone/Download the project**

   ```bash

**Use Case**: Teacher logs "Feeling overwhelmed with grading" → AI detects stress + suggests peer support + offers 2-min breathing exercise   cd "d:\Documents\UNI\3rd  Year\Application of Ai\Project"

   ```

### 4️⃣ AI-Powered Scheduling & Intelligent Rewards

**🤖 Tech:** Groq Llama 3.3 70B (Schedule Optimization + Personalization)2. **Install Tesseract OCR** (for Windows)

   - Download from: https://github.com/UB-Mannheim/tesseract/wiki

- 🤖 **AI Schedule Analysis**: Detects time conflicts, workload imbalances, and deadline clusters   - Install to default location (C:\Program Files\Tesseract-OCR)

- 💡 **Optimal Time Suggestions**: AI recommends best class times based on cognitive science & existing schedule   - Add to PATH environment variable

- 🏆 **Gamified Rewards**: Points & badges system for students/teachers

- 🎯 **AI Reward Coach**: Personalized motivation based on activity patterns & performance3. **Install Python dependencies**

   ```bash

**Use Case**: Adding new Math class → AI suggests "Tuesday 10 AM" to avoid back-to-back classes + balance workload   pip install -r requirements.txt

   ```

## 🚀 Quick Start

4. **Configure API Key**

### Prerequisites   - Your API key is already set in `.env` file

- Python 3.11+   - Model: `llama-3.3-70b-versatile`

- [Groq API Key](https://console.groq.com/)

- [Gemini API Key](https://makersuite.google.com/app/apikey)5. **Run the application**

   ```bash

### Installation   streamlit run app.py

   ```

1. **Clone the repository**

```bash6. **Open in browser**

git clone https://github.com/Sambhav-Ja1n/AI-Powered-Productivity-engine-for-teachers.git   - The app will automatically open at `http://localhost:8501`

cd AI-Powered-Productivity-engine-for-teachers

```## 📁 Project Structure



2. **Create virtual environment**```

```bashProject/

python -m venv .venv├── app.py                      # Main Streamlit application

.venv\Scripts\activate  # Windows├── assessment_grading.py       # Feature 1: AI Grading

source .venv/bin/activate  # macOS/Linux├── content_recommender.py      # Feature 2: Content & Q/A

```├── wellbeing_monitor.py        # Feature 3: Wellbeing

├── scheduling_rewards.py       # Feature 4: Scheduling & Rewards

3. **Install dependencies**├── requirements.txt            # Python dependencies

```bash├── .env                        # Environment variables

pip install -r requirements.txt└── data/                       # Data storage (auto-created)

```    ├── schedule.json

    └── rewards.json

4. **Set up API keys**```

Copy `.env.example` to `.env` and add your API keys:

```bash## 🎯 Usage Guide

cp .env.example .env

```### Dashboard

- Overview of all metrics

Edit `.env` file:- Today's schedule

```env- Upcoming assignments

GROQ_API_KEY=your_groq_api_key_here- Quick actions

GEMINI_API_KEY=your_gemini_api_key_here

LLAMA_MODEL=llama-3.3-70b-versatile### AI Assessment & Grading

```1. **Text Grading**: Enter student answer and model answer

2. **Image Grading**: Upload handwritten homework for OCR + grading

5. **Run the application**3. **Self-Evaluation**: Students get hints without answers

```bash

streamlit run app.py### Content Recommender

```1. **Find Resources**: Search by topic, level, teaching method

2. **Q&A Agent**: Ask subject questions with context

6. **Access the app**3. **Worksheets**: Generate practice questions automatically

Open your browser to `http://localhost:8501`

### Well-being Monitor

## 📁 Project Structure1. **Daily Reflection**: Log feelings and get analysis

2. **View Reports**: Track wellbeing trends over time

```3. **Peer Support**: Get suggestions for connecting with colleagues

AI-Powered-Productivity-engine-for-teachers/

├── app.py                      # Main Streamlit application### Scheduling & Rewards

├── assessment_grading.py       # Feature 1: AI Grading with OCR1. **View Schedule**: See classes and assignments

├── content_recommender.py      # Feature 2: RAG & Q/A System2. **Add Events**: Create new classes or assignments

├── wellbeing_monitor.py        # Feature 3: Well-being Monitoring3. **Rewards**: Track points and badges

├── scheduling_rewards.py       # Feature 4: Scheduling & Gamification4. **Leaderboard**: See top performers

├── requirements.txt            # Python dependencies

├── .env.example                # Environment variables template## 🔧 Configuration

├── .gitignore                  # Git ignore rules

└── README.md                   # This file### Environment Variables (.env)

``````

GROQ_API_KEY=your_api_key_here

## 🛠️ Technology StackLLAMA_MODEL=llama-3.3-70b-versatile

DEBUG=True

### AI & MLMAX_FILE_SIZE=10485760

- **Groq API** - Fast LLM inference (Llama 3.3 70B Versatile)```

- **Google Gemini Vision** - OCR and multimodal understanding

- **Sentence Transformers** - Semantic text embeddings (all-MiniLM-L6-v2)### Adding Learning Resources

- **RAG Architecture** - Retrieval Augmented Generation for accurate Q&AEdit `content_recommender.py` and add to `SAMPLE_RESOURCES`:

```python

### Framework & UI{

- **Streamlit** - Interactive web application framework    "topic": "Your Topic",

- **Python 3.11+** - Core programming language    "content": "Description of the resource...",

- **NumPy** - Vector operations and similarity calculations    "resource_type": "video/article/worksheet",

    "difficulty": "beginner/intermediate/advanced",

### Storage & Processing    "teaching_method": "visual/interactive/discussion"

- **JSON** - Persistent data storage for schedules, rewards, and well-being data}

- **PIL/Pillow** - Image processing for homework uploads```

- **Datetime** - Time management and scheduling logic

### Customizing Badges

## 📊 System ArchitectureEdit `scheduling_rewards.py` in `_get_default_badges()` method.



```## 🎨 Technologies Used

User Interface (Streamlit)

         ↓- **Frontend**: Streamlit

┌────────┴────────────────┐- **AI Model**: Groq (Llama 3.3-70b-versatile)

│    Feature Layer        │- **OCR**: EasyOCR / Pytesseract

├─────────────────────────┤- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)

│ 1. Assessment & Grading │ → Gemini Vision → Groq LLM- **Storage**: JSON files

│ 2. Content Recommender  │ → Sentence Transformer → Groq LLM (RAG)- **Image Processing**: Pillow, OpenCV

│ 3. Well-being Monitor   │ → Groq LLM → Sentiment Analysis

│ 4. Scheduling & Rewards │ → Groq LLM → AI Optimization## 📊 Demo Data

└─────────────────────────┘

         ↓The system includes sample data for testing:

   JSON Storage + Cache- 5 learning resources across different subjects

```- Badge system with 6 different achievements

- Default teacher and student profiles

## 🎯 Use Cases

## 🐛 Troubleshooting

### For Teachers

- ✅ Grade homework **10x faster** with AI-powered evaluation### OCR Not Working

- ✅ Get **instant resource recommendations** for any topic- Ensure Tesseract is installed and in PATH

- ✅ **Track and improve mental well-being** with sentiment analysis- For EasyOCR: First run will download models (~100MB)

- ✅ **Optimize schedule** with AI-powered conflict detection

### API Errors

### For Students- Check your Groq API key in `.env`

- ✅ **Self-evaluate homework** before submission- Verify you have API credits

- ✅ Get **personalized study materials** matched to learning style- Check internet connection

- ✅ **Track progress** with gamification and badges

- ✅ Access **AI Q&A** for quick explanations### Import Errors

- Run: `pip install -r requirements.txt`

## 🔧 Technical Highlights- Make sure you're using Python 3.8+



### Feature 1: Multimodal AI Grading### Streamlit Issues

- Uses Gemini Vision's multimodal capabilities to read handwritten text- Clear cache: `streamlit cache clear`

- Prompt engineering for accurate text extraction- Restart the app

- Groq LLM analyzes student responses against model answers

- Generates structured feedback with scores, strengths, and improvements## 🚀 Deployment



### Feature 2: RAG-Based Q&A### Local Development

- Vector embeddings create semantic search space (384 dimensions)```bash

- Cosine similarity finds most relevant resourcesstreamlit run app.py

- Retrieved context augments LLM prompt for accurate answers```

- Citations link back to original sources

### Deploy to Streamlit Cloud

### Feature 3: Sentiment Analysis1. Push code to GitHub

- NLP techniques extract emotional tone from reflections2. Connect to Streamlit Cloud

- Stress level detection using pattern recognition3. Add secrets (API keys) in settings

- Personalized interventions based on severity4. Deploy!

- Longitudinal tracking for trend analysis

### Deploy to Lovable.dev

### Feature 4: AI Schedule Optimization1. Create new project on lovable.dev

- LLM analyzes schedule for conflicts and balance2. Upload all Python files

- Applies cognitive science principles (spacing effect, peak hours)3. Configure environment variables

- Gamification engine with badge unlock prediction4. Launch application

- Personalized motivation based on user patterns

## 📝 Notes

## 🔐 Security & Privacy

- First OCR operation will download models (1-2 minutes)

- ✅ API keys stored in `.env` (never committed to Git)- Embedding model downloads on first use (~80MB)

- ✅ Personal data (schedules, reflections) excluded from repository- All data stored in `data/` folder (JSON files)

- ✅ Secure API communication with Groq and Gemini- Images processed temporarily and deleted

- ✅ Local data storage for privacy

## 🤝 Contributing

## 📝 API Keys Setup

This is a hackathon MVP. Feel free to extend with:

### Groq API Key- Database integration (PostgreSQL, MongoDB)

1. Visit [Groq Console](https://console.groq.com/)- Email notifications

2. Sign up / Log in- Mobile app version

3. Navigate to API Keys section- Advanced analytics

4. Create new key- Multi-language support

5. Copy to `.env` file

## 📄 License

### Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)MIT License - Free for educational and commercial use

2. Sign in with Google account

3. Click "Create API Key"## 👥 Authors

4. Copy to `.env` file

Built for AI Application Course Project - 3rd Year

## 🚧 Troubleshooting

## 🙏 Acknowledgments

### Issue: "ModuleNotFoundError"

```bash- Groq for fast LLM inference

pip install -r requirements.txt- EasyOCR for handwriting recognition

```- Streamlit for rapid UI development

- Sentence Transformers for embeddings

### Issue: "API Key Error"

- Check `.env` file exists and has correct keys---

- Verify API keys are valid on respective platforms

**Ready to revolutionize teaching with AI!** 🎓✨

### Issue: "PermissionError: temp_homework.png"
- File is automatically cleaned up after processing
- Restart the app if error persists

### Issue: "Streamlit not found"
```bash
pip install streamlit
```

## 🎓 Educational Impact

This system addresses key challenges in education:
- **Teacher Burnout**: Automates grading and reduces administrative workload
- **Personalized Learning**: Adapts resources to individual student needs
- **Mental Health**: Proactively monitors and supports teacher well-being
- **Efficiency**: AI-optimized schedules save time and reduce conflicts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👥 Author

- **Sambhav Jain** - [GitHub](https://github.com/Sambhav-Ja1n)

## 🙏 Acknowledgments

- **Groq** for providing fast LLM inference infrastructure
- **Google** for Gemini Vision API
- **Sentence Transformers** team for pre-trained embedding models
- **Streamlit** community for the amazing web framework

## 📧 Contact

For questions, suggestions, or collaboration opportunities:
- GitHub: [@Sambhav-Ja1n](https://github.com/Sambhav-Ja1n)
- Repository: [AI-Powered-Productivity-engine-for-teachers](https://github.com/Sambhav-Ja1n/AI-Powered-Productivity-engine-for-teachers)

---

**⭐ Star this repo if you find it helpful!**

**Made with ❤️ for teachers and students everywhere**
