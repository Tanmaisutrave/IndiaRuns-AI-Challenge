import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="AI Candidate Discovery & Ranking System",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Candidate Discovery & Ranking System")

st.subheader("India Runs Data & AI Challenge")

st.markdown("""
This solution ranks AI/ML candidates using:

- AI Skills Matching
- Experience Analysis
- Career History Evaluation
- Recruiter Engagement Signals
- Interview Reliability Signals
- Explainable AI Ranking
""")
submission = pd.read_csv("output/final_submission.csv")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Top Candidates",
        len(submission)
    )

with col2:
    st.metric(
        "Best Score",
        round(submission["score"].max(),2)
    )

with col3:
    st.metric(
        "Submission Status",
        "Valid"
    )
st.divider()

st.header("🏆 Top 100 Ranked Candidates")

st.dataframe(
    submission,
    use_container_width=True,
    height=450
)

st.download_button(
    label="📥 Download Submission CSV",
    data=submission.to_csv(index=False),
    file_name="final_submission.csv",
    mime="text/csv"
)
st.divider()

st.header("👤 Candidate Explorer")

selected_candidate = st.selectbox(
    "Select Candidate ID",
    submission["candidate_id"]
)

candidate = submission[
    submission["candidate_id"] == selected_candidate
].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.info(f"🆔 Candidate ID: {candidate['candidate_id']}")
    st.success(f"🏆 Rank: #{candidate['rank']}")

with col2:
    st.warning(f"⭐ Score: {candidate['score']:.4f}")

# ===========================================
# Why This Candidate Was Selected
# ===========================================

st.markdown("---")

st.markdown("""
<h1 style='font-size:48px;font-weight:bold;'>
📄 Why This Candidate Was Selected
</h1>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="
background:#1d263b;
padding:35px;
border-left:8px solid #2ecc71;
border-radius:20px;
box-shadow:0px 0px 18px rgba(46,204,113,0.25);
">

<h1 style="color:#2ecc71;font-size:42px;margin-bottom:20px;">
🏆 Selection Justification
</h1>

<p style="font-size:28px;
line-height:1.8;
color:white;
margin-bottom:25px;">
{candidate["reasoning"]}
</p>

<hr style="border:1px solid #556070;">

<h2 style="color:#2ecc71;
margin-top:30px;
font-size:36px;">
✅ Key Reasons
</h2>

<ul style="
font-size:25px;
line-height:2.0;
color:white;
">

<li>Strong AI / ML skill match</li>

<li>Relevant experience for the role</li>

<li>High recruiter engagement</li>

<li>Strong interview completion history</li>

<li>Excellent overall ranking score</li>

</ul>

</div>
""", unsafe_allow_html=True)

# ===========================================
# Analytics Dashboard
# ===========================================

st.markdown("---")

st.markdown("""
<h1 style='font-size:48px;font-weight:bold;'>
📊 Analytics Dashboard
</h1>
""", unsafe_allow_html=True)

# ------------------------------------------
# Chart 1 : Candidate Score Distribution
# ------------------------------------------

st.subheader("Candidate Score Distribution")

bins = [0,0.2,0.4,0.6,0.8,1.0]

distribution = pd.cut(
    submission["score"],
    bins=bins,
    include_lowest=True
).value_counts().sort_index()

fig = px.bar(
    x=[
        "0 - 0.2",
        "0.2 - 0.4",
        "0.4 - 0.6",
        "0.6 - 0.8",
        "0.8 - 1.0"
    ],
    y=distribution.values,
    text=distribution.values
)

fig.update_layout(
    xaxis_title="Score Range",
    yaxis_title="Number of Candidates",
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------
# Chart 2 : Top 20 Candidate Scores
# ------------------------------------------

st.subheader("Top 20 Candidate Scores")

top20 = submission.head(20)

fig = px.bar(
    top20,
    x="candidate_id",
    y="score",
    text="score"
)

fig.update_layout(
    template="plotly_dark",
    height=500,
    xaxis_tickangle=-35,
    xaxis_title="Candidate ID",
    yaxis_title="Score"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------
# Chart 3 : Rank vs Score
# ------------------------------------------

st.subheader("Rank vs Score")

fig = px.line(
    submission,
    x="rank",
    y="score",
    markers=True
)

fig.update_layout(
    template="plotly_dark",
    height=500,
    xaxis_title="Rank",
    yaxis_title="Score"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------
# Chart 4 : Candidate Score Segments
# ------------------------------------------

st.subheader("Candidate Score Segments")

labels = [
    "0 - 0.2",
    "0.2 - 0.4",
    "0.4 - 0.6",
    "0.6 - 0.8",
    "0.8 - 1.0"
]

fig = px.pie(
    values=distribution.values,
    names=labels,
    hole=0
)

fig.update_layout(
    template="plotly_dark",
    height=550
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------
# Footer
# ------------------------------------------

st.success(
    "Top 100 candidates successfully ranked using a Hybrid AI Ranking Engine with Explainable AI reasoning."
)

st.markdown("---")

st.markdown("""
<div style="
background: linear-gradient(135deg,#0f172a,#1e293b);
padding:28px;
border-radius:18px;
border:1px solid #2d3748;
text-align:center;
box-shadow:0 0 12px rgba(0,255,170,0.08);
margin-top:20px;
">

<h2 style="
color:#22c55e;
margin-bottom:10px;
font-size:28px;">
✅ AI Candidate Discovery & Ranking Completed
</h2>

<p style="
font-size:18px;
color:#d1d5db;
margin-bottom:18px;">
Successfully ranked the <b>Top 100 AI/ML Candidates</b> using a
<b>Hybrid AI Ranking Engine</b> powered by skill matching,
career analysis, behavioral signals, recruiter engagement,
and explainable AI reasoning.
</p>

<hr style="border:1px solid #374151; margin:18px 0;">

<div style="
display:flex;
justify-content:space-around;
font-size:16px;
color:#9ca3af;">

<div>
<b style="color:white;">📊 Candidates Ranked</b><br>
100
</div>

<div>
<b style="color:white;">🧠 Ranking Signals</b><br>
23
</div>

<div>
<b style="color:white;">🤖 AI Explainability</b><br>
Enabled
</div>

<div>
<b style="color:white;">✔ Submission</b><br>
Valid
</div>

</div>

<br>

<p style="
font-size:14px;
color:#6b7280;
margin-top:12px;">
Developed for the <b>India Runs Data & AI Challenge</b> • Powered by Python, Pandas, Plotly & Streamlit
</p>

</div>
""", unsafe_allow_html=True)