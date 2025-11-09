# 🏗️ SYSTEM ARCHITECTURE

## 📊 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                            │
│                     (Streamlit Web App)                          │
│                         app.py                                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ├─────────────────────────────────────┐
                         │                                     │
┌────────────────────────▼────────┐   ┌────────────────────────▼──────┐
│   FEATURE 1: GRADING            │   │   FEATURE 2: RECOMMENDER      │
│   assessment_grading.py         │   │   content_recommender.py      │
│                                 │   │                               │
│   ┌─────────────────────┐      │   │   ┌──────────────────────┐   │
│   │  Text Grading       │      │   │   │  Vector Search       │   │
│   │  - Parse input      │      │   │   │  - Embeddings        │   │
│   │  - Groq LLM grade   │      │   │   │  - Similarity calc   │   │
│   └─────────────────────┘      │   │   └──────────────────────┘   │
│                                 │   │                               │
│   ┌─────────────────────┐      │   │   ┌──────────────────────┐   │
│   │  OCR Processing     │      │   │   │  Q&A Agent           │   │
│   │  - EasyOCR          │      │   │   │  - RAG retrieval     │   │
│   │  - Text extraction  │      │   │   │  - Groq generation   │   │
│   └─────────────────────┘      │   │   └──────────────────────┘   │
│                                 │   │                               │
│   ┌─────────────────────┐      │   │   ┌──────────────────────┐   │
│   │  Self-Evaluation    │      │   │   │  Worksheet Gen       │   │
│   │  - Hint generation  │      │   │   │  - Dynamic questions │   │
│   │  - No spoilers      │      │   │   │  - Answer keys       │   │
│   └─────────────────────┘      │   │   └──────────────────────┘   │
└─────────────────────────────────┘   └───────────────────────────────┘
                         │                                     │
                         ├─────────────────────────────────────┘
                         │
┌────────────────────────▼────────┐   ┌────────────────────────▼──────┐
│   FEATURE 3: WELLBEING          │   │   FEATURE 4: SCHEDULING       │
│   wellbeing_monitor.py          │   │   scheduling_rewards.py       │
│                                 │   │                               │
│   ┌─────────────────────┐      │   │   ┌──────────────────────┐   │
│   │  Sentiment Analysis │      │   │   │  Schedule Manager    │   │
│   │  - Groq LLM         │      │   │   │  - Classes           │   │
│   │  - Stress detection │      │   │   │  - Assignments       │   │
│   └─────────────────────┘      │   │   └──────────────────────┘   │
│                                 │   │                               │
│   ┌─────────────────────┐      │   │   ┌──────────────────────┐   │
│   │  Interventions      │      │   │   │  Rewards Engine      │   │
│   │  - Suggestions      │      │   │   │  - Points system     │   │
│   │  - Peer support     │      │   │   │  - Badge logic       │   │
│   └─────────────────────┘      │   │   └──────────────────────┘   │
│                                 │   │                               │
│   ┌─────────────────────┐      │   │   ┌──────────────────────┐   │
│   │  Trend Reports      │      │   │   │  Leaderboard         │   │
│   │  - History tracking │      │   │   │  - Rankings          │   │
│   │  - Visualizations   │      │   │   │  - Competition       │   │
│   └─────────────────────┘      │   │   └──────────────────────┘   │
└─────────────────────────────────┘   └───────────────────────────────┘
                         │                                     │
                         └─────────────┬───────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────┐
│                         INTEGRATIONS                                 │
├──────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐ │
│  │  Groq API   │  │  EasyOCR    │  │  Sentence   │  │  JSON     │ │
│  │             │  │             │  │  Transform  │  │  Storage  │ │
│  │  LLM        │  │  OCR        │  │  Embeddings │  │  Files    │ │
│  │  Inference  │  │  Engine     │  │  Model      │  │           │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Diagrams

### Feature 1: Grading Flow
```
Student Homework (Image/Text)
        │
        ▼
┌───────────────┐
│  Input Layer  │
└───────┬───────┘
        │
        ├─── Text? ──────────┐
        │                    ▼
        ├─── Image? ─────► EasyOCR ────► Extract Text
        │                    │
        └────────────────────┴──────────┐
                                        ▼
                            ┌───────────────────────┐
                            │   Groq LLM Grading    │
                            │   - Compare answers   │
                            │   - Generate feedback │
                            └───────────┬───────────┘
                                        ▼
                            ┌───────────────────────┐
                            │   Format Response     │
                            │   - Score             │
                            │   - Feedback          │
                            │   - Suggestions       │
                            └───────────┬───────────┘
                                        ▼
                                Display to User
```

### Feature 2: RAG Flow
```
User Query
    │
    ▼
┌────────────────────┐
│  Query Embedding   │
│  (Sent. Transform) │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Vector Search     │
│  - Cosine Sim      │
│  - Top K results   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Groq LLM          │
│  - Context + Query │
│  - Generate Answer │
└─────────┬──────────┘
          │
          ▼
    Response + Sources
```

### Feature 3: Wellbeing Flow
```
Teacher Reflection
        │
        ▼
┌──────────────────┐
│  Groq LLM        │
│  - Sentiment     │
│  - Emotions      │
│  - Stress        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Analysis Result │
│  - Score: -1~+1  │
│  - Level: L/M/H  │
└────────┬─────────┘
         │
         ├─── Store in History
         │
         ▼
┌──────────────────┐
│  Generate        │
│  Interventions   │
│  (Groq LLM)      │
└────────┬─────────┘
         │
         ▼
  Display Suggestions
```

### Feature 4: Rewards Flow
```
User Action (Complete Task)
        │
        ▼
┌──────────────────┐
│  Award Points    │
│  - Base points   │
│  - Bonus (early) │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Check Badges    │
│  - Evaluate      │
│  - Unlock new    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Update Storage  │
│  - rewards.json  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Update UI       │
│  - Leaderboard   │
│  - Profile       │
└──────────────────┘
```

---

## 🗄️ Data Models

### Grading Result
```json
{
  "score": 8,
  "percentage": 80.0,
  "feedback": "Good understanding...",
  "strengths": ["Clear explanation", "Correct formula"],
  "improvements": ["Add more details", "Include examples"],
  "mistakes": ["Minor spelling error"],
  "extracted_text": "..." // only for OCR
}
```

### Learning Resource
```json
{
  "topic": "Photosynthesis",
  "content": "Description...",
  "resource_type": "video",
  "difficulty": "beginner",
  "teaching_method": "visual",
  "similarity_score": 0.85
}
```

### Wellbeing Analysis
```json
{
  "sentiment_score": -0.3,
  "stress_level": "high",
  "emotions": ["frustrated", "determined"],
  "concerns": ["Time management", "Student behavior"],
  "positive_aspects": ["Completed lesson plan"],
  "overall_assessment": "Challenging day..."
}
```

### User Profile
```json
{
  "user_id": "teacher_123",
  "name": "Ms. Smith",
  "total_points": 1245,
  "badges": ["early_bird", "dedicated_teacher"],
  "history": [
    {
      "timestamp": "2025-11-06T10:00:00",
      "points": 20,
      "reason": "Graded assignment"
    }
  ],
  "stats": {
    "graded_count": 47,
    "materials_created": 12
  }
}
```

### Schedule Entry
```json
{
  "id": "class_1",
  "name": "Mathematics 101",
  "day": "Monday",
  "start_time": "09:00",
  "end_time": "10:30",
  "subject": "Mathematics",
  "room": "Room 101",
  "created_at": "2025-11-06T08:00:00"
}
```

---

## 🔌 API Interactions

### Groq API Calls

#### 1. Grading
```python
POST https://api.groq.com/openai/v1/chat/completions
Headers: Authorization: Bearer {API_KEY}
Body: {
  "model": "llama-3.3-70b-versatile",
  "messages": [
    {"role": "system", "content": "You are an expert grader..."},
    {"role": "user", "content": "Grade this: ..."}
  ],
  "temperature": 0.3,
  "max_tokens": 1000
}
```

#### 2. Q&A
```python
POST https://api.groq.com/openai/v1/chat/completions
Body: {
  "model": "llama-3.3-70b-versatile",
  "messages": [
    {"role": "system", "content": "You are a helpful teacher..."},
    {"role": "user", "content": "Context: ...\n\nQuestion: ..."}
  ],
  "temperature": 0.4,
  "max_tokens": 600
}
```

#### 3. Sentiment Analysis
```python
POST https://api.groq.com/openai/v1/chat/completions
Body: {
  "model": "llama-3.3-70b-versatile",
  "messages": [
    {"role": "system", "content": "You are a wellbeing analyst..."},
    {"role": "user", "content": "Analyze: ..."}
  ],
  "temperature": 0.3,
  "max_tokens": 800
}
```

---

## 📦 Module Dependencies

```
app.py
├── assessment_grading.py
│   ├── groq
│   ├── easyocr
│   └── PIL
├── content_recommender.py
│   ├── groq
│   ├── sentence_transformers
│   └── numpy
├── wellbeing_monitor.py
│   ├── groq
│   └── datetime
└── scheduling_rewards.py
    ├── datetime
    ├── json
    └── pathlib

Common Dependencies:
├── streamlit (UI framework)
├── python-dotenv (env management)
└── os (system operations)
```

---

## 🎯 Performance Characteristics

### Latency (Average)
- **Text Grading:** 3-5 seconds
- **OCR + Grading:** 5-8 seconds (first run: +10s for model load)
- **Recommendations:** 3-6 seconds (first run: +15s for embeddings)
- **Q&A:** 2-4 seconds
- **Sentiment:** 2-4 seconds
- **Scheduling:** <100ms (local JSON)
- **Rewards:** <100ms (local JSON)

### Resource Usage
- **RAM:** 2-4 GB (embeddings + OCR models)
- **Disk:** 1-2 GB (models cached)
- **Network:** ~1KB per API call (request) + 2-5KB (response)
- **API Tokens:** 100-1500 tokens per call

### Scalability
- **Concurrent Users:** 10-50 (local), unlimited (cloud)
- **Requests/min:** Limited by Groq rate limits (free tier: ~30/min)
- **Storage:** JSON scales to ~10,000 entries before DB needed

---

## 🔐 Security Considerations

### Current Implementation
- ✅ API key in .env (not in code)
- ✅ No credentials in UI
- ✅ Local data storage

### Production Recommendations
- [ ] Add user authentication
- [ ] Encrypt .env file
- [ ] Use secrets management (HashiCorp Vault)
- [ ] HTTPS for deployment
- [ ] Rate limiting per user
- [ ] Input sanitization
- [ ] SQL injection prevention (when DB added)
- [ ] GDPR compliance (data retention policies)

---

## 🚀 Deployment Architecture

### Local Development (Current)
```
┌──────────────────┐
│  Local Machine   │
│                  │
│  ┌────────────┐ │
│  │ Streamlit  │ │
│  │ Server     │ │
│  │ :8501      │ │
│  └────────────┘ │
│                  │
│  ┌────────────┐ │
│  │ JSON Files │ │
│  │ ./data/    │ │
│  └────────────┘ │
└────────┬─────────┘
         │
         ▼
    Groq API (Cloud)
```

### Cloud Deployment (Recommended)
```
┌────────────────────────────────────┐
│  Streamlit Cloud / Heroku          │
│                                    │
│  ┌──────────────────────────────┐ │
│  │  Streamlit App               │ │
│  │  (Auto-scaling)              │ │
│  └──────────────────────────────┘ │
│                                    │
│  ┌──────────────────────────────┐ │
│  │  Environment Variables       │ │
│  │  (Secrets Management)        │ │
│  └──────────────────────────────┘ │
└────────┬───────────────────────────┘
         │
         ├──────────────┐
         ▼              ▼
    Groq API      PostgreSQL DB
    (Cloud)       (Managed Service)
```

---

## 🧩 Extension Points

### Easy Additions
1. **More Subjects:** Add to dropdown lists
2. **More Resources:** Extend SAMPLE_RESOURCES
3. **More Badges:** Add to badge definitions
4. **Email Notifications:** Add SMTP integration
5. **PDF Export:** Add ReportLab

### Medium Complexity
1. **Database Migration:** Replace JSON with PostgreSQL
2. **User Auth:** Add login system
3. **Multi-language:** i18n support
4. **Analytics Dashboard:** Add charts with Plotly
5. **Mobile App:** React Native wrapper

### Advanced Features
1. **LMS Integration:** Canvas/Moodle APIs
2. **Video Analysis:** Lecture transcription + Q&A
3. **Plagiarism Detection:** Content similarity
4. **Predictive Analytics:** Student performance forecasting
5. **Voice Interface:** Speech-to-text for reflections

---

## 📊 System Metrics

### Code Quality
- **Lines of Code:** ~1,850
- **Files:** 9 Python files
- **Functions:** ~50 total
- **Classes:** 4 main classes
- **Comments:** ~15% of code
- **Modularity:** High (4 independent features)

### Test Coverage
- **Manual Testing:** 100% of features
- **Unit Tests:** Not implemented (MVP)
- **Integration Tests:** Manual demo flows
- **Performance Tests:** Informal benchmarking

### Documentation
- **README:** Comprehensive
- **Guides:** 3 detailed guides
- **Code Comments:** Moderate
- **API Docs:** Inline docstrings

---

**This architecture supports rapid development, easy maintenance, and seamless scaling!** 🏗️
