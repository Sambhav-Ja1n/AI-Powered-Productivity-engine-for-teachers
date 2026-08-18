# AI Teacher Assistant

An AI-based productivity tool for teachers that combines grading, learning resources, teacher well-being tracking, and schedule management in one application.

This started as a hackathon/project idea around a simple problem: **teachers spend a lot of time on repetitive work outside the actual teaching.** I wanted to see how much of that workflow could be handled with AI without making the system unnecessarily complicated.

The current version is an MVP built with Python and Streamlit.

---

## What it does

### 1. AI Assessment & Grading

The grading module can evaluate both normal text answers and handwritten homework.

For handwritten work, the system first extracts the text using a vision/OCR model and then sends the answer for evaluation.

It can provide:

* score
* feedback
* strengths
* areas for improvement
* self-evaluation hints
* MCQ analysis

**Used:** Gemini Vision, Groq / Llama 3.3 70B

---

### 2. Content Recommendation & Q/A

The content module uses embeddings and RAG to find relevant educational material before generating an answer.

A student can search for a topic or ask a question, and the system retrieves relevant resources and uses them as context.

It can also generate practice worksheets and recommend resources based on the student's level.

**Used:** Sentence Transformers, RAG, Groq / Llama 3.3 70B

---

### 3. Teacher Well-being

This part is fairly simple by design.

A teacher can write a short daily reflection. The system analyzes the text and looks for sentiment/stress patterns.

It then provides things such as:

* basic sentiment analysis
* 7-day trends
* small stress-relief suggestions
* peer-support suggestions

This isn't intended to be a medical or psychological system. It's mainly a way of experimenting with how AI could be used to notice patterns in everyday workload and reflections.

**Used:** Groq / Llama 3.3 70B

---

### 4. Scheduling & Rewards

The scheduling module keeps track of classes and assignments and can look for conflicts or workload imbalance.

There is also a small gamification component with:

* points
* badges
* leaderboard
* activity-based rewards

The data for the current MVP is stored locally using JSON.

---

## How the system is put together

At a high level, the application looks like this:

```text
                    Streamlit App
                         |
        +----------------+----------------+
        |                |                |
     Grading          Content          Well-being
        |                |                |
 Gemini Vision       Embeddings         LLM
        |                |                |
        +----------------+----------------+
                         |
                    Groq / Llama
                         |
                  Scheduling/Rewards
```

Different modules use different approaches depending on the problem rather than sending everything directly to an LLM.

---

## Tech Stack

**Language**

* Python 3.11+

**AI / ML**

* Groq
* Llama 3.3 70B
* Google Gemini Vision
* Sentence Transformers
* RAG
* OCR

**Application**

* Streamlit

**Other**

* NumPy
* Pillow
* OpenCV
* JSON
* python-dotenv

---

## Project Structure

```text
AI-Powered-Productivity-engine-for-teachers/
│
├── app.py
├── assessment_grading.py
├── content_recommender.py
├── wellbeing_monitor.py
├── scheduling_rewards.py
├── requirements.txt
├── .env.example
├── .gitignore
│
└── data/
    ├── schedule.json
    └── rewards.json
```

Each major feature is kept in its own Python file so that the application can be extended without putting everything into `app.py`.

---

## Running it locally

### 1. Clone the repository

```bash
git clone https://github.com/Sambhav-Ja1n/AI-Powered-Productivity-engine-for-teachers.git

cd AI-Powered-Productivity-engine-for-teachers
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API keys

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
LLAMA_MODEL=llama-3.3-70b-versatile
```

### 5. Start the application

```bash
streamlit run app.py
```

The app should then be available at:

```text
http://localhost:8501
```

---

## A few technical details

### Grading

The grading pipeline roughly follows:

```text
Homework image
      ↓
Vision / OCR
      ↓
Extracted answer
      ↓
LLM evaluation
      ↓
Score + feedback
```

### RAG

For the recommendation system:

```text
User question
      ↓
Embedding
      ↓
Similarity search
      ↓
Relevant resources
      ↓
LLM + retrieved context
      ↓
Answer
```

The current implementation uses `all-MiniLM-L6-v2` for embeddings.

---

## Current limitations

This is still an MVP, so there are a few obvious areas that need work.

* Data is currently stored locally in JSON.
* The recommendation dataset is relatively small.
* OCR quality depends on the uploaded image.
* The well-being module is intentionally basic.
* Authentication and multi-user support aren't implemented yet.
* API keys are required for the AI features.
* The scheduling system could be made considerably more sophisticated.

These are also some of the areas I'd work on if turning this into a larger application.

---

## Possible next steps

Some things I'd like to experiment with next:

* PostgreSQL instead of JSON storage
* user authentication
* better analytics
* email notifications
* mobile version
* multilingual support
* better schedule optimization
* larger educational resource database

---

## Why I built it

The interesting part of this project for me wasn't just connecting an LLM to a UI.

It was trying to use different AI techniques for different parts of the same workflow:

* vision models for handwritten work
* embeddings for finding relevant resources
* RAG for grounded answers
* LLMs for evaluation and analysis
* sentiment analysis for reflections
* optimization for scheduling

It's still a work in progress, but it gave me a good opportunity to work with several parts of an AI application in one project.

---

## Author

**Sambhav Jain**

B.Tech CSE (AI), Bennett University

GitHub: [@Sambhav-Ja1n](https://github.com/Sambhav-Ja1n)

---

## License

MIT License
