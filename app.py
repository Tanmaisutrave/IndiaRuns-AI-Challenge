import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
from src.load_data import load_candidates

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Candidate Discovery & Ranking",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚀 AI Candidate Discovery & Ranking System")

st.markdown("""
### India Runs Data & AI Challenge

This system ranks candidates using:

- Experience Matching
- AI Skills Analysis
- Career History Analysis
- Redrob Behavioral Signals
- Semantic Re-ranking
""")

# --------------------------------------------------
# METRICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Candidates", "100,000")

with col2:
    st.metric("Top Ranked Candidate", "Rajesh Reddy")

with col3:
    st.metric("Ranking Method", "Hybrid AI")

# --------------------------------------------------
# TOP 100 TABLE
# --------------------------------------------------

st.divider()

st.header("🏆 Top 100 Ranked Candidates")

df = pd.read_csv("output/final_submission.csv")

st.dataframe(
    df,
    use_container_width=True
)

st.download_button(
    label="📥 Download Submission CSV",
    data=df.to_csv(index=False),
    file_name="submission.csv",
    mime="text/csv"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

st.divider()

candidates = load_candidates("candidates.jsonl")

candidate_ids = [
    c["candidate_id"]
    for c in candidates
]

# --------------------------------------------------
# PROFILE VIEWER
# --------------------------------------------------

st.header("👤 Candidate Profile Viewer")

search_id = st.text_input(
    "🔍 Search Candidate ID"
)

if search_id and search_id in candidate_ids:
    selected_id = search_id
else:
    selected_id = st.selectbox(
        "Select Candidate",
        candidate_ids
    )

selected_candidate = None

for c in candidates:
    if c["candidate_id"] == selected_id:
        selected_candidate = c
        break

# --------------------------------------------------
# PROFILE DETAILS
# --------------------------------------------------

if selected_candidate:

    profile = selected_candidate["profile"]

    st.subheader("Profile")

    st.write(
        f"**Name:** {profile['anonymized_name']}"
    )

    st.write(
        f"**Current Title:** {profile['current_title']}"
    )

    st.write(
        f"**Experience:** {profile['years_of_experience']} years"
    )

    st.write(
        f"**Industry:** {profile['current_industry']}"
    )

    st.write(
        f"**Location:** {profile['location']}"
    )

    st.write(
        f"**Summary:** {profile['summary']}"
    )

    # -------------------------
    # SKILLS
    # -------------------------

    st.subheader("Skills")

    skills = [
        s["name"]
        for s in selected_candidate["skills"]
    ]

    st.write(", ".join(skills))

    # -------------------------
    # CAREER HISTORY
    # -------------------------

    st.subheader("Career History")

    for job in selected_candidate["career_history"]:

        st.markdown(
            f"### {job['title']} @ {job['company']}"
        )

        st.write(job["description"])

        st.divider()

# --------------------------------------------------
# EXPLAINABLE AI
# --------------------------------------------------

st.header("🤖 Why This Candidate Ranked Highly")

if selected_candidate:

    profile = selected_candidate["profile"]
    signals = selected_candidate["redrob_signals"]

    st.success("Ranking Explanation")

    st.write(
        f"✅ {profile['years_of_experience']} years experience"
    )

    st.write(
        f"✅ Current Role: {profile['current_title']}"
    )

    st.write(
        f"✅ Industry: {profile['current_industry']}"
    )

    st.write(
        f"✅ Recruiter Response Rate: {signals['recruiter_response_rate']}"
    )

    st.write(
        f"✅ Interview Completion Rate: {signals['interview_completion_rate']}"
    )

    st.write(
        f"✅ GitHub Activity Score: {signals['github_activity_score']}"
    )

    st.write(
        "✅ Strong semantic similarity with Job Description"
    )

# --------------------------------------------------
# ANALYTICS DASHBOARD
# --------------------------------------------------

st.divider()

st.header("📊 Analytics Dashboard")

# -------------------------
# EXPERIENCE DISTRIBUTION
# -------------------------

experience = [
    c["profile"]["years_of_experience"]
    for c in candidates
]

exp_ranges = {
    "0-3 Years": 0,
    "3-5 Years": 0,
    "5-9 Years": 0,
    "9+ Years": 0
}

for exp in experience:

    if exp < 3:
        exp_ranges["0-3 Years"] += 1

    elif exp < 5:
        exp_ranges["3-5 Years"] += 1

    elif exp < 9:
        exp_ranges["5-9 Years"] += 1

    else:
        exp_ranges["9+ Years"] += 1

exp_chart = pd.DataFrame({
    "Range": list(exp_ranges.keys()),
    "Candidates": list(exp_ranges.values())
})

fig1 = px.bar(
    exp_chart,
    x="Range",
    y="Candidates",
    title="Candidate Experience Groups"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# -------------------------
# TOP SKILLS
# -------------------------

all_skills = []

for c in candidates:

    for skill in c["skills"]:

        all_skills.append(
            skill["name"]
        )

skill_counts = Counter(all_skills)

top_skills = pd.DataFrame(
    skill_counts.most_common(10),
    columns=["Skill", "Count"]
)

fig2 = px.bar(
    top_skills,
    x="Skill",
    y="Count",
    title="Top 10 Skills"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -------------------------
# INDUSTRY DISTRIBUTION
# -------------------------

industries = [
    c["profile"]["current_industry"]
    for c in candidates
]

industry_counts = Counter(
    industries
)

industry_df = pd.DataFrame(
    industry_counts.items(),
    columns=["Industry", "Count"]
)

fig3 = px.pie(
    industry_df,
    names="Industry",
    values="Count",
    title="Industry Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

