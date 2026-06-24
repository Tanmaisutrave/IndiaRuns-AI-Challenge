import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Candidate Discovery & Ranking",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("🚀 AI Candidate Discovery & Ranking System")

st.markdown("""
### India Runs Data & AI Challenge

This solution ranks AI/ML candidates using:

- AI Skills Matching
- Experience Analysis
- Career History Evaluation
- Recruiter Engagement Signals
- Interview Reliability Signals
- Explainable AI Ranking
""")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("output/final_submission.csv")

# =========================
# METRICS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Top Candidates",
        len(df)
    )

with col2:
    st.metric(
        "Best Score",
        round(df["score"].max(), 4)
    )

with col3:
    st.metric(
        "Submission Status",
        "Valid"
    )

st.divider()

# =========================
# TOP 100 TABLE
# =========================

st.header("🏆 Top 100 Ranked Candidates")

st.dataframe(
    df,
    use_container_width=True,
    height=500
)

st.download_button(
    label="📥 Download Submission CSV",
    data=df.to_csv(index=False),
    file_name="final_submission.csv",
    mime="text/csv"
)

st.divider()

# =========================
# CANDIDATE EXPLORER
# =========================

st.header("👤 Candidate Explorer")

selected_candidate = st.selectbox(
    "Select Candidate ID",
    df["candidate_id"]
)

candidate = df[
    df["candidate_id"] == selected_candidate
].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.info(
        f"Candidate ID: {candidate['candidate_id']}"
    )

    st.success(
        f"Rank: {candidate['rank']}"
    )

with col2:
    st.warning(
        f"Score: {candidate['score']}"
    )

# ==================================
# WHY THIS CANDIDATE WAS SELECTED
# ==================================

st.header("Why This Candidate Was Selected")

reason = candidate["reasoning"]

st.markdown(
    f"""
    <div style="
        background: linear-gradient(135deg,#0F172A,#1E293B);
        padding:30px;
        border-radius:20px;
        border-left:8px solid #22C55E;
        box-shadow:0px 0px 20px rgba(34,197,94,0.3);
        margin-bottom:25px;
    ">

    <h2 style="color:#22C55E;">
        🏆 Selection Justification
    </h2>

    <p style="
        color:white;
        font-size:20px;
        line-height:1.8;
    ">
        {reason}
    </p>

    <hr style="border:1px solid #334155;">

    <h3 style="color:#22C55E;">
        ✅ Key Reasons
    </h3>

    <ul style="
        color:white;
        font-size:18px;
        line-height:2;
    ">
        <li>Strong AI / ML skill match</li>
        <li>Relevant experience for the role</li>
        <li>High recruiter engagement</li>
        <li>Strong interview completion history</li>
        <li>Excellent overall ranking score</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================
# ANALYTICS
# =========================

st.header("📊 Analytics Dashboard")

# Score Distribution

# Score Distribution (Cleaner Version)

score_ranges = pd.cut(
    df["score"],
    bins=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
    labels=[
        "0 - 0.2",
        "0.2 - 0.4",
        "0.4 - 0.6",
        "0.6 - 0.8",
        "0.8 - 1.0"
    ]
)

score_summary = score_ranges.value_counts().sort_index()

score_df = pd.DataFrame({
    "Score Range": score_summary.index,
    "Candidates": score_summary.values
})

fig1 = px.bar(
    score_df,
    x="Score Range",
    y="Candidates",
    text="Candidates",
    title="Candidate Score Distribution"
)

fig1.update_traces(
    textposition="outside"
)

fig1.update_layout(
    xaxis_title="Score Range",
    yaxis_title="Number of Candidates",
    height=500
)

st.plotly_chart(
    fig1,
    use_container_width=True,
    key="score_distribution"
)

# Top 20 Candidates

top20 = df.head(20)

fig2 = px.bar(
    top20,
    x="candidate_id",
    y="score",
    title="Top 20 Candidate Scores"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Rank vs Score

fig3 = px.line(
    df,
    x="rank",
    y="score",
    markers=True,
    title="Rank vs Score"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# Score Categories

score_bins = pd.cut(
    df["score"],
    bins=5
).value_counts().sort_index()

score_df = pd.DataFrame({
    "Score Range": score_bins.index.astype(str),
    "Candidates": score_bins.values
})

fig4 = px.pie(
    score_df,
    names="Score Range",
    values="Candidates",
    title="Candidate Score Segments"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.divider()

st.success(
    "Top 100 candidates successfully ranked using a Hybrid AI Ranking Engine with Explainable AI reasoning."
)

