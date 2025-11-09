# AI Teacher Assistant System - File Structure

```
d:\Documents\UNI\3rd Year\Application of Ai\Project\
│
├── 📄 app.py                          # Main Streamlit application (run this!)
│
├── 🔧 Feature Modules:
│   ├── assessment_grading.py          # Feature 1: AI Grading with OCR
│   ├── content_recommender.py         # Feature 2: RAG-based Q&A
│   ├── wellbeing_monitor.py           # Feature 3: Wellbeing tracking
│   └── scheduling_rewards.py          # Feature 4: Schedule & Gamification
│
├── ⚙️ Configuration:
│   ├── .env                           # API keys and settings
│   └── requirements.txt               # Python dependencies
│
├── 🚀 Launch Scripts:
│   ├── run.bat                        # Windows batch script
│   ├── run.ps1                        # PowerShell script
│   └── test_system.py                 # Test all components
│
├── 📚 Documentation:
│   └── README.md                      # Full documentation
│
└── 💾 Data (auto-created):
    ├── schedule.json                  # Schedule and assignments
    └── rewards.json                   # Points and badges
```

## Quick Start Commands

### Option 1: Double-click run.bat
Just double-click the `run.bat` file!

### Option 2: PowerShell
```powershell
.\run.ps1
```

### Option 3: Manual
```bash
pip install -r requirements.txt
streamlit run app.py
```

## First Time Setup

1. ✅ API Key already configured in `.env`
2. ✅ All code files created
3. ⏳ Install dependencies: `pip install -r requirements.txt`
4. ⏳ Run the app: `streamlit run app.py`

## What Each File Does

### app.py (Main Application)
- Streamlit UI with 5 tabs (Dashboard + 4 features)
- Integrates all features
- Handles user interactions
- ~700 lines of UI code

### assessment_grading.py
- Text-based homework grading
- OCR with EasyOCR for handwritten work
- Student self-evaluation hints
- Detailed feedback generation
- ~250 lines

### content_recommender.py
- Vector embeddings with Sentence Transformers
- RAG (Retrieval Augmented Generation)
- Q&A agent for questions
- Worksheet generator
- Sample knowledge base included
- ~300 lines

### wellbeing_monitor.py
- Sentiment analysis with Groq LLM
- Stress level detection
- Micro-intervention suggestions
- Peer support recommendations
- Wellbeing trend reports
- ~250 lines

### scheduling_rewards.py
- Class schedule management
- Assignment tracking
- Points and badges system
- Leaderboard
- JSON-based storage
- ~350 lines

## Total: ~1,850 lines of working code!
