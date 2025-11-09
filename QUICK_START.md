# ⚡ QUICK START GUIDE

## 🚀 GET STARTED IN 3 STEPS

### Step 1: Open Terminal
Press `Win + R`, type `powershell`, press Enter

### Step 2: Navigate to Project
```powershell
cd "d:\Documents\UNI\3rd  Year\Application of Ai\Project"
```

### Step 3: Run the App
```powershell
streamlit run app.py
```

**That's it!** The app will open in your browser automatically.

---

## 🌐 ACCESS THE APP

Once running, open:
- **Local:** http://localhost:8501
- **Network:** http://10.120.113.45:8501

---

## 📱 WHAT YOU'LL SEE

### Dashboard (Home)
- 4 metric cards
- Today's schedule
- Upcoming assignments
- Quick action buttons

### Main Features (Left Sidebar)
1. **📝 AI Assessment & Grading**
   - Grade text homework
   - Grade handwritten homework (OCR)
   - Student self-evaluation

2. **📚 Content Recommender & Q/A**
   - Find learning resources
   - Ask questions (get AI answers)
   - Generate practice worksheets

3. **💚 Teacher Well-being Monitor**
   - Daily reflection analysis
   - Stress level detection
   - Get helpful interventions
   - View wellbeing trends

4. **📅 Scheduling & Rewards**
   - View schedule
   - Add classes/assignments
   - Track points and badges
   - See leaderboard

---

## 🎯 TRY THESE FIRST

### 1. Test AI Grading (2 minutes)
1. Click "📝 AI Assessment & Grading" in sidebar
2. Select "Biology" as subject
3. Paste this correct answer:
   ```
   Photosynthesis converts light energy to chemical energy using chlorophyll in plants
   ```
4. Paste this student answer:
   ```
   Plants make food from sunlight
   ```
5. Click "🎯 Grade Answer"
6. Watch AI provide instant feedback!

### 2. Ask a Question (1 minute)
1. Click "📚 Content Recommender & Q/A"
2. Go to "❓ Q&A Agent" tab
3. Ask: "What is photosynthesis?"
4. Click "💬 Get Answer"
5. See AI answer with sources!

### 3. Check Your Wellbeing (2 minutes)
1. Click "💚 Teacher Well-being Monitor"
2. Write any reflection about your day
3. Click "💭 Analyze Reflection"
4. Get sentiment analysis + stress level + interventions!

### 4. Add an Assignment (1 minute)
1. Click "📅 Scheduling & Rewards"
2. Go to "➕ Add Events" tab
3. Select "Assignment"
4. Fill in details
5. Click "➕ Add Assignment"
6. See it appear in schedule!

---

## 🆘 TROUBLESHOOTING

### Problem: "Module not found"
**Solution:**
```powershell
pip install -r requirements.txt
```
Wait for all packages to install, then run app again.

### Problem: App is slow first time
**Reason:** Downloading AI models (~200MB)
**Solution:** Wait 2-3 minutes on first run. Subsequent runs are fast!

### Problem: OCR not working
**Reason:** Model downloading
**Solution:** Wait for first OCR operation to complete (~1-2 min)

### Problem: Can't access app
**Solution:** Make sure you see "You can now view your Streamlit app" message
Then open: http://localhost:8501

---

## 📚 MORE INFORMATION

- **Full Documentation:** See `README.md`
- **Complete Guide:** See `COMPLETE_GUIDE.md`
- **Demo Instructions:** See `DEMO_SCRIPT.md`
- **Architecture:** See `ARCHITECTURE.md`
- **Project Summary:** See `PROJECT_SUMMARY.md`

---

## 🎓 WHAT'S INCLUDED

### ✅ All 4 Features Working
- AI grading with OCR
- RAG-powered Q&A
- Wellbeing monitoring
- Rewards & scheduling

### ✅ Sample Data Ready
- 5 learning resources
- 6 badge types
- Demo users configured

### ✅ API Configured
- Groq API key: Already set in `.env`
- Model: llama-3.3-70b-versatile

---

## 💡 PRO TIPS

1. **First Run:** Let models download (2-3 min)
2. **Testing:** Try all tabs in each feature
3. **Demo:** Use DEMO_SCRIPT.md for presentation
4. **Customize:** Edit sample resources in code
5. **Share:** Use network URL to show on other devices

---

## 🎬 DEMO READY

Everything is set up for:
- ✅ Live demo
- ✅ Testing all features
- ✅ Hackathon presentation
- ✅ Course project submission

---

## 📞 NEED HELP?

1. Run diagnostic: `python test_system.py`
2. Check logs in terminal
3. Review `README.md` for details
4. Check API status at console.groq.com

---

## ⚡ QUICK COMMANDS

```powershell
# Navigate to project
cd "d:\Documents\UNI\3rd  Year\Application of Ai\Project"

# Install dependencies
pip install -r requirements.txt

# Test system
python test_system.py

# Run app
streamlit run app.py

# Clear cache (if issues)
streamlit cache clear
```

---

## 🎯 NEXT STEPS

After exploring the app:
1. ✅ Test all 4 features
2. ✅ Upload sample homework image
3. ✅ Generate a practice worksheet
4. ✅ Check wellbeing analysis
5. ✅ Earn some badges

Then:
- Read `DEMO_SCRIPT.md` for presentation tips
- Check `COMPLETE_GUIDE.md` for full details
- Review `ARCHITECTURE.md` for technical overview

---

## 🎉 YOU'RE READY!

**Your AI Teacher Assistant System is:**
- ✅ Built
- ✅ Running
- ✅ Demo-ready
- ✅ Production-quality

**Access it now at:** http://localhost:8501

---

**🎓 Happy Teaching with AI! 🚀**

*Built for hackathons, designed for real classrooms.*
