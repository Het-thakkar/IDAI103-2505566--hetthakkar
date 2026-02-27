import streamlit as st
from pose_module import detect_pose
from scoring import analyze_form
from ai_module import (
    generate_training_plan,
    generate_form_feedback,
    generate_nutrition_plan,
    generate_tactical_advice,
    generate_recovery_plan,
    generate_mental_focus_routine,
    generate_warmup_cooldown,
    generate_hydration_plan,
    generate_strength_program,
    generate_progress_report,
)
import pandas as pd

st.set_page_config(page_title="CoachBot AI", layout="wide", page_icon="🏆")

st.title("🏆 CoachBot AI — Intelligent Youth Sports Coaching Platform")
st.caption("Powered by Generative AI | NextGen Sports Lab")

tabs = st.tabs([
    "📋 Training Plan",
    "🤸 Pose Analysis",
    "📊 Analytics",
    "🥗 Nutrition",
    "🎯 Tactical Advice",
    "🩹 Recovery",
    "🧠 Mental Focus",
    "💧 Hydration",
    "💪 Strength",
    "📈 Progress Report"
])

# ── TAB 1: TRAINING PLAN ──────────────────────────────────────────────────────
with tabs[0]:
    st.header("📋 AI Training Plan Generator")
    st.write("Generate a personalized 7-day training plan based on your sport and goals.")

    col1, col2 = st.columns(2)
    with col1:
        sport = st.selectbox("Select Sport", ["Football", "Cricket", "Basketball", "Athletics", "Swimming", "Tennis"])
        position = st.text_input("Your Position (e.g. Striker, Bowler, Point Guard)")
    with col2:
        injury = st.text_input("Injury History (leave blank if none)")
        goal = st.text_input("Training Goal (e.g. Build stamina, Improve speed)")

    if st.button("🚀 Generate Training Plan"):
        if sport and goal:
            with st.spinner("CoachBot is creating your plan..."):
                plan = generate_training_plan(sport, position, injury, goal)
            st.success("Your Training Plan is Ready!")
            st.write(plan)
        else:
            st.warning("Please fill in Sport and Goal fields.")

# ── TAB 2: POSE ANALYSIS ─────────────────────────────────────────────────────
with tabs[1]:
    st.header("🤸 Live Pose Analysis")
    st.write("Activate your webcam to analyze your exercise form in real time.")

    if st.button("▶️ Start Pose Detection"):
        with st.spinner("Opening webcam — press Q in the camera window to stop..."):
            pose_data = detect_pose()

        if pose_data:
            scoring_data = analyze_form(pose_data)
            feedback = generate_form_feedback(pose_data, scoring_data)

            col1, col2, col3 = st.columns(3)
            col1.metric("Form Score", f"{scoring_data['score']}/100")
            col2.metric("Grade", scoring_data['grade'])
            col3.metric("Hip Angle", f"{pose_data['hip_angle']}°")

            st.subheader("📝 Form Feedback")
            for tip in scoring_data['feedback']:
                st.write(tip)

            st.subheader("🤖 AI Biomechanical Advice")
            st.write(feedback)
        else:
            st.warning("No pose detected. Make sure your full body is visible to the camera.")

# ── TAB 3: ANALYTICS ─────────────────────────────────────────────────────────
with tabs[2]:
    st.header("📊 Performance Analytics")
    st.write("Track your form improvement across training sessions.")

    history = pd.DataFrame({
        "session": [1, 2, 3, 4, 5],
        "form_score": [60, 70, 78, 85, 92]
    })

    st.line_chart(history.set_index("session"))
    st.dataframe(history.rename(columns={"session": "Session", "form_score": "Form Score"}))

# ── TAB 4: NUTRITION ──────────────────────────────────────────────────────────
with tabs[3]:
    st.header("🥗 Personalized Nutrition Guide")
    st.write("Get a weekly meal plan tailored to your sport and dietary needs.")

    col1, col2 = st.columns(2)
    with col1:
        n_sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics", "Swimming"], key="n_sport")
        n_age = st.number_input("Age", min_value=10, max_value=25, value=15)
    with col2:
        n_diet = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan", "Gluten-Free"])
        n_calories = st.number_input("Daily Calorie Goal (kcal)", min_value=1200, max_value=4000, value=2200)

    n_allergies = st.text_input("Food Allergies or Restrictions (optional)")

    if st.button("🥗 Generate Nutrition Plan"):
        with st.spinner("Preparing your nutrition guide..."):
            plan = generate_nutrition_plan(n_sport, n_age, n_diet, n_calories, n_allergies)
        st.success("Nutrition Plan Ready!")
        st.write(plan)

# ── TAB 5: TACTICAL ADVICE ───────────────────────────────────────────────────
with tabs[4]:
    st.header("🎯 Tactical Coaching Advice")
    st.write("Get position-specific tactical coaching to level up your game.")

    t_sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics"], key="t_sport")
    t_position = st.text_input("Your Position", key="t_pos")
    t_skill = st.text_input("Skill to Improve (e.g. Dribbling, Bowling accuracy, Rebounding)")

    if st.button("🎯 Get Tactical Advice"):
        if t_skill:
            with st.spinner("Analyzing tactics..."):
                advice = generate_tactical_advice(t_sport, t_position, t_skill)
            st.success("Tactical Advice Ready!")
            st.write(advice)
        else:
            st.warning("Please enter a skill to improve.")

# ── TAB 6: RECOVERY PLAN ─────────────────────────────────────────────────────
with tabs[5]:
    st.header("🩹 Injury Recovery Plan")
    st.write("Get a safe, phased recovery schedule designed around your injury.")

    r_injury = st.text_input("Describe Your Injury (e.g. Knee sprain, Shoulder strain)")
    r_sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics"], key="r_sport")
    r_goal = st.text_input("Recovery Goal (e.g. Return to full training in 4 weeks)")

    if st.button("🩹 Generate Recovery Plan"):
        if r_injury:
            with st.spinner("Building your recovery plan..."):
                plan = generate_recovery_plan(r_injury, r_sport, r_goal)
            st.success("Recovery Plan Ready!")
            st.write(plan)
        else:
            st.warning("Please describe your injury.")

# ── TAB 7: MENTAL FOCUS ──────────────────────────────────────────────────────
with tabs[6]:
    st.header("🧠 Mental Focus & Mindset Routine")
    st.write("Build mental strength and confidence before your next big event.")

    m_sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics"], key="m_sport")
    m_event = st.text_input("Upcoming Event (e.g. School tournament, Regional championship)")
    m_days = st.number_input("Days Until Event", min_value=1, max_value=90, value=7)

    if st.button("🧠 Generate Mental Focus Routine"):
        if m_event:
            with st.spinner("Preparing your mindset routine..."):
                routine = generate_mental_focus_routine(m_sport, m_event, m_days)
            st.success("Mental Focus Routine Ready!")
            st.write(routine)
        else:
            st.warning("Please enter your upcoming event.")

# ── TAB 8: HYDRATION PLAN ────────────────────────────────────────────────────
with tabs[7]:
    st.header("💧 Hydration & Electrolyte Strategy")
    st.write("Stay optimally hydrated before, during, and after training.")

    h_sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics"], key="h_sport")
    h_climate = st.selectbox("Climate / Weather", ["Hot & Humid", "Hot & Dry", "Mild", "Cold"])
    h_duration = st.number_input("Session Duration (minutes)", min_value=20, max_value=180, value=60)
    h_weight = st.number_input("Body Weight (kg)", min_value=30, max_value=120, value=60)

    if st.button("💧 Generate Hydration Plan"):
        with st.spinner("Calculating hydration needs..."):
            plan = generate_hydration_plan(h_sport, h_climate, h_duration, h_weight)
        st.success("Hydration Plan Ready!")
        st.write(plan)

# ── TAB 9: STRENGTH PROGRAM ──────────────────────────────────────────────────
with tabs[8]:
    st.header("💪 Sport-Specific Strength Program")
    st.write("Build targeted strength for your sport and position.")

    s_sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics"], key="s_sport")
    s_position = st.text_input("Position", key="s_pos")
    s_level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
    s_equipment = st.text_input("Available Equipment (e.g. Dumbbells, Resistance bands, Gym)")

    if st.button("💪 Generate Strength Program"):
        with st.spinner("Designing your strength program..."):
            program = generate_strength_program(s_sport, s_position, s_level, s_equipment)
        st.success("Strength Program Ready!")
        st.write(program)

# ── TAB 10: PROGRESS REPORT ──────────────────────────────────────────────────
with tabs[9]:
    st.header("📈 Athlete Progress Report")
    st.write("Get an AI-generated summary of your training journey so far.")

    p_sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics"], key="p_sport")
    p_position = st.text_input("Position", key="p_pos")
    p_sessions = st.number_input("Sessions Completed", min_value=1, max_value=100, value=10)
    p_avg_score = st.slider("Average Form Score", 0, 100, 75)
    p_goals = st.text_input("Your Original Goals")

    if st.button("📈 Generate Progress Report"):
        if p_goals:
            with st.spinner("Generating your progress report..."):
                report = generate_progress_report(p_sport, p_position, p_sessions, p_avg_score, p_goals)
            st.success("Progress Report Ready!")
            st.write(report)
        else:
            st.warning("Please enter your original goals.")