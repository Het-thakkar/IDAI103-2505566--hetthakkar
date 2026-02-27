# 🏆 CoachBot AI — Smart Fitness Assistance Web App

> **CRS:** Artificial Intelligence | **Course:** Generative AI | **Assessment:** Summative (Individual)  
> **Scenario 2:** Creating a Smart Fitness Assistance Web App Powered by Generative AI

---

## 📌 Project Overview

**CoachBot AI** is a Generative AI-powered virtual sports coaching web application built using **Python**, **Streamlit**, and the **OpenAI GPT-4o-mini** model. It is designed to bridge the gap in professional coaching for young and under-resourced athletes by providing personalized, AI-driven fitness plans, tactical advice, injury recovery support, and nutrition guidance — all through a simple, accessible web interface.

The application was developed as part of the **NextGen Sports Lab** scenario, where the goal is to empower the next generation of athletes with AI-driven tools regardless of their access to professional coaches.

---

## 🎯 Problem Definition & Objectives

### The Problem
Many aspiring young athletes — especially in under-resourced regions — do not have access to professional coaches or personalized fitness programs. This gap leads to ineffective training, increased injury risk, and slower development.

### Our Solution
CoachBot AI acts as a **24/7 virtual coach** that:
- Generates **personalized training plans** based on sport, position, and goals
- Provides **real-time biomechanical feedback** using pose detection
- Offers **position-specific tactical advice** for various sports
- Creates **injury-safe recovery schedules**
- Delivers **custom nutrition and hydration plans**
- Supports **mental focus and mindset** coaching
- Tracks **athlete progress** over multiple sessions

### Key Objectives
- Empower youth with AI-based personal training
- Generate adaptive fitness routines based on physical condition and position
- Encourage safety, motivation, and nutrition awareness
- Make professional-level coaching accessible to all young athletes

---

## 🔬 Research Findings

### Sport-Specific Training
Research shows that training must be tailored to the demands of specific sports and positions. A goalkeeper requires different conditioning than a striker; a fast bowler needs different strength work than a batsman. Generic training plans are ineffective and increase injury risk (IJISRT, 2023).

### AI in Sports Coaching
Generative AI models can simulate the knowledge of experienced coaches by synthesizing sport science research, biomechanical principles, and nutritional guidelines. Studies have shown that AI-generated coaching advice can match the quality of entry-level coaching when prompts are well-engineered (IBM, 2024).

### Youth Sports Injuries
Common youth injuries include knee sprains, ankle strains, and shoulder overuse injuries. Safe return-to-sport protocols require a phased approach with low-impact exercises before returning to full training (NCBI, 2021).

### Pose Estimation Technology
MediaPipe's pose estimation can accurately detect key body landmarks in real time, enabling automated form analysis for exercises like squats, lunges, and sprint mechanics (Google MediaPipe, 2023).

### Key References
- IJISRT (2023) — : https://www.ijisrt.com/artificial-intelligence-powered-fitness-web-app
- IBM (2024) — *Develop AI Personal Trainer*: https://www.ibm.com/think/tutorials/develop-ai-personal-trainer-with-llama-4-watsonx-ai
- NCBI (2021) — *Youth Sports Injury Prevention*: https://www.ncbi.nlm.nih.gov/books/NBK566046/
- ExRx (2024) — *Workout Menu & Exercise Database*: https://exrx.net/Lists/WorkoutMenu
- EatRight (2024) — *Sports Nutrition Guidelines*: https://www.eatright.org/
- TIJER (2023) — *AI in Fitness Applications*: https://tijer.org/tijer/papers/TIJERC001307.pdf
- EREPS (2024) — *How AI Can Be Used in Fitness*: https://www.ereps.eu/news/how-can-ai-be-used-fitness

---

## 🤖 Model Used

| Parameter | Value |
|-----------|-------|
| **Model** | GPT-4o-mini (OpenAI) |
| **API** | OpenAI Chat Completions API |
| **Framework** | Streamlit (Python) |
| **Pose Detection** | MediaPipe + OpenCV |

### Hyperparameter Tuning

| Feature | Temperature | Reasoning |
|---------|-------------|-----------|
| Training Plan | 0.6 | Balanced — creative but structured |
| Form Feedback | 0.5 | Conservative — safety-focused |
| Nutrition Plan | 0.6 | Balanced meal planning |
| Tactical Advice | 0.7 | More creative coaching tips |
| Recovery Plan | 0.3 | Conservative — injury safety critical |
| Mental Focus | 0.7 | Creative motivational content |
| Warm-up/Cooldown | 0.5 | Standard exercise protocols |
| Hydration Plan | 0.5 | Factual hydration science |
| Strength Program | 0.6 | Structured but adaptable |
| Progress Report | 0.7 | Motivating and personalized tone |

**Why temperature matters:**
- **Lower (0.3):** Safe, conservative, factually accurate — used for injury/recovery content
- **Medium (0.5–0.6):** Balanced creativity and accuracy — used for training/nutrition
- **Higher (0.7–0.9):** Creative, motivating, varied — used for tactical and mental coaching

---

## 📝 Prompt Engineering — 10 Features & Prompts

### Prompt 1 — Personalized 7-Day Training Plan
```
You are CoachBot AI, an expert youth sports coach.
Generate a detailed 7-day training plan for:
Sport: {sport}, Position: {position},
Injury History: {injury}, Goal: {goal}.
Include daily warm-up, sport-specific drills, strength, recovery, and safety notes.
```

### Prompt 2 — Real-Time Form Feedback (Pose Analysis)
```
Athlete performed a {exercise}.
Knee Angle: {knee_angle}°, Hip Angle: {hip_angle}°,
Form Score: {score}/100, Grade: {grade}, Issues: {feedback}.
Provide biomechanical corrections and injury-safe advice for a young athlete.
```

### Prompt 3 — Weekly Nutrition Guide
```
Create a weekly nutrition guide for a {age}-year-old {sport} player.
Diet: {diet_type}, Calories: {calorie_goal} kcal, Allergies: {allergies}.
Include all meals, snacks, and hydration tips for each day.
Focus on performance, recovery, and healthy growth.
```

### Prompt 4 — Position-Specific Tactical Advice
```
As a tactical coach, give detailed advice for a {position} in {sport}
to improve {skill_to_improve}.
Include drills, decision-making strategies, and common mistakes to avoid.
```

### Prompt 5 — Injury Recovery Schedule
```
Create a safe recovery schedule for a {sport} player with {injury}.
Goal: {recovery_goal}.
Include phases, safe low-impact exercises, exercises to AVOID,
return-to-sport timeline, and warning signs of re-injury.
Prioritize safety and gradual progression.
```

### Prompt 6 — Mental Focus & Mindset Routine
```
Create a mental focus routine for a {sport} player preparing
for {event_type} in {days_until_event} days.
Include visualization techniques, breathing exercises,
positive affirmations, and strategies for handling nerves and pressure.
```

### Prompt 7 — Warm-up & Cooldown Routine
```
Generate a warm-up and cooldown routine for a {position} in {sport}
for a {session_type} session.
Warm-up (15 mins): dynamic stretches, activation drills, sport-specific movements.
Cooldown (10 mins): static stretches, breathing, foam rolling suggestions.
```

### Prompt 8 — Hydration & Electrolyte Strategy
```
Create a hydration strategy for a {sport} player ({body_weight_kg}kg)
training for {session_duration} mins in {climate} weather.
Include pre, during, and post-session hydration,
electrolyte tips, and warning signs of dehydration.
```

### Prompt 9 — Sport-Specific Strength Program
```
Design a strength program for a {fitness_level} {position} in {sport}
with {equipment} available.
Include weekly schedule, key muscle groups, sets/reps/rest,
progressive overload guidelines, and youth safety tips (growth plate awareness).
```

### Prompt 10 — Athlete Progress Report
```
Generate a motivating progress report for a {position} in {sport}.
Sessions completed: {sessions_completed}, Average form score: {avg_score}/100,
Original goals: {goals}.
Include achievements, areas for improvement, focus for next block,
and an encouraging message to keep the athlete motivated.
```

---

## ✅ Validated Model Responses (Simulation Results)

### Test 1 — Training Plan (Football Striker, Build Stamina)
**Input:** Sport: Football | Position: Striker | Goal: Build stamina | Injury: None

**Output Summary:** The model generated a structured 7-day plan including Monday interval runs, Tuesday technical drills, Wednesday strength (squats, lunges), Thursday tactical positioning, Friday speed work, Saturday match simulation, Sunday active recovery. Safety notes included gradual intensity increase and hydration reminders. Output was coherent, sport-specific, and age-appropriate. ✅

### Test 2 — Recovery Plan (Knee Sprain, Cricket)
**Input:** Injury: Knee sprain | Sport: Cricket | Goal: Return in 4 weeks

**Output Summary:** Model correctly avoided high-impact exercises, suggested pool-based cardio, resistance band work, and hamstring stretches. Included a 3-phase recovery timeline (inflammation → strengthening → return to sport). Temperature 0.3 kept advice conservative and safe. ✅

### Test 3 — Nutrition Plan (15-year-old, Football, Vegetarian)
**Input:** Age: 15 | Sport: Football | Diet: Vegetarian | Calories: 2200 kcal

**Output Summary:** Full 7-day plan with breakfast, lunch, dinner and snacks. Included iron-rich vegetarian sources (lentils, spinach), complex carbs pre-training, protein recovery meals. Hydration: 2.5L/day recommended. ✅

### Test 4 — Pose Analysis Feedback (Squat, Score 60/100)
**Input:** Exercise: Squat | Knee angle: 65° | Hip angle: 75° | Score: 60/100

**Output Summary:** AI correctly identified over-deep knee bend as injury risk, recommended box squats to control depth, suggested glute activation exercises. Encouraging tone suitable for youth athlete. ✅

### Test 5 — Mental Focus (School Tournament, 7 days)
**Input:** Sport: Football | Event: School tournament | Days: 7

**Output Summary:** Day-by-day mental preparation plan including visualization scripts, pre-match breathing (4-7-8 technique), positive affirmations, and strategies for managing first-match nerves. Creative and motivating tone. ✅

**Overall Model Performance:** Responses were consistently coherent, position-sensitive, and personalized. Temperature tuning effectively controlled output creativity vs. safety. All 10 features produced relevant, high-quality responses.

---

## 🗂️ Project Structure

```
CoachBotAI/
│
├── app.py              # Main Streamlit application (10 feature tabs)
├── ai_module.py        # OpenAI API integration & all 10 prompt functions
├── pose_module.py      # MediaPipe pose detection & angle calculation
├── scoring.py          # Form scoring logic & progress visualization
├── analytics.py        # Performance analytics helpers
├── requirements.txt    # Python dependencies
├── .env                # API key (not committed to GitHub)
└── README.md           # This file
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- OpenAI API key (with active credits)

### Step 1 — Clone the Repository
```bash
git clone https://github.com/YourUsername/YourRepoName
cd YourRepoName
```

### Step 2 — Create Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Set API Key
Open `ai_module.py` and add your key directly:
```python
client = OpenAI(api_key="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")
```

### Step 5 — Run the App
```bash
streamlit run app.py
```

Open: https://zewgqsjdggjqe5iytwcju6.streamlit.app/

---

## 📦 Dependencies (requirements.txt)

```
streamlit==1.32.0
mediapipe==0.10.14
opencv-python==4.8.0.76
numpy==1.26.4
openai==1.30.1
pandas==2.2.2
matplotlib==3.8.4
python-dotenv==1.0.1
```

---

 API key in :
   ```
   OPENAI_API_KEY = "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"
   ```
6. Click **Deploy** and share your public URL

---

## 🔐 Security Note

- Never commit your API key to GitHub
- Add `.env` to your `.gitignore`
- Rotate your key immediately if accidentally shared publicly

---

## 👤 Student Details

| Field | Details |
|-------|---------|
| **Full Name** | [Het Thakkar] |
| **CRS** | Artificial Intelligence |
| **School** | [Udgam School For Children ] |
---

## 📄 License

MIT License — for academic use only.
