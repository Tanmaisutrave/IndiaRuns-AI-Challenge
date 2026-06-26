# 🚀 AI Candidate Discovery & Ranking System

## 🏆 India Runs Data & AI Challenge 2026

An **Explainable AI-powered Candidate Ranking Platform** that intelligently discovers, evaluates, and ranks the **Top 100 AI/ML candidates** from a dataset of **100,000 candidate profiles** using hybrid AI scoring, behavioral intelligence, and career analysis.

---

## 🌐 Live Demo

**Streamlit Dashboard**

https://indiaruns-ai-challenge-zfhv3zgvlcxqhfwxog3pzb.streamlit.app/

---

## 📌 Problem Statement

The challenge aims to identify and rank the most suitable candidates for a specialized AI/ML role from a large dataset containing candidate profiles, skills, career history, education, and behavioral signals.

The system must generate a transparent and explainable ranking while producing a submission containing the **Top 100 candidates**.

---

# ✨ Solution Overview

This project implements a **Hybrid AI Ranking Engine** that combines multiple candidate signals to generate an overall ranking score.

The ranking pipeline evaluates each candidate using:

* 🤖 AI/ML Skill Matching
* 💼 Professional Experience
* 📈 Career History Analysis
* 🧠 Behavioral Signal Intelligence
* 🏢 Product Company Experience
* 🎓 Education Analysis
* 💻 GitHub Activity
* 📄 Explainable AI Reasoning

Finally, the candidates are ranked and the **Top 100 profiles** are selected.

---

# 🧠 Ranking Methodology

## 1️⃣ Experience Evaluation

Candidates receive scores based on their years of relevant professional experience.

---

## 2️⃣ AI Skill Matching

The system identifies and scores high-value AI/ML skills including:

* Machine Learning
* Deep Learning
* NLP
* Embeddings
* Vector Search
* Semantic Search
* RAG
* Fine-tuning LLMs
* Recommendation Systems
* FAISS
* Milvus
* Qdrant
* BM25
* PyTorch
* TensorFlow
* LangChain
* LlamaIndex
* MLOps
* Apache Spark
* Kafka

---

## 3️⃣ Career History Analysis

Career descriptions and previous job roles are analyzed for experience related to:

* AI Engineering
* Machine Learning
* Search Systems
* Retrieval Systems
* Recommendation Engines
* Learning-to-Rank
* Vector Databases
* Large Language Models
* Semantic Search

---

## 4️⃣ Behavioral Signal Analysis

The ranking engine incorporates multiple behavioral signals provided by Redrob.

### Signals Used

* Recruiter Response Rate
* Interview Completion Rate
* Profile Completeness
* Saved by Recruiters
* Profile Views
* Search Appearance
* Open To Work Status
* Notice Period
* GitHub Activity
* Connection Count
* Endorsements
* Skill Assessment Scores
* Offer Acceptance Rate
* Applications Submitted
* Average Response Time
* Verified Email
* Verified Phone
* LinkedIn Connected
* Preferred Work Mode
* Relocation Preference

---

## 5️⃣ Product Company Experience

Candidates with experience in well-known product companies receive additional weighting during ranking.

---

## 6️⃣ Education Analysis

Educational background is also considered using:

* Degree
* Field of Study
* Institution Tier

---

# 🤖 Explainable AI

Every ranked candidate includes an automatically generated explanation describing why they were selected.

The explanation considers:

* AI/ML Skills
* Experience
* Career Relevance
* Recruiter Engagement
* Interview Reliability
* Behavioral Signals
* Overall Ranking Justification

This makes the ranking process transparent and interpretable.

---

# 📊 Interactive Dashboard

A Streamlit dashboard has been developed to visualize rankings and candidate insights.

## Dashboard Features

* 🏆 Top 100 Candidate Rankings
* 👤 Candidate Explorer
* 🤖 Explainable AI Decision
* 📄 Selection Justification
* 📈 Score Breakdown
* 📊 Candidate Score Distribution
* 📊 Top 20 Candidate Scores
* 📉 Rank vs Score
* 🥧 Candidate Score Segments
* 📥 Download Submission CSV

---

# 🛠 Technology Stack

## Programming Language

* Python

## Data Processing

* Pandas
* NumPy

## Machine Learning

* Sentence Transformers

## Dashboard

* Streamlit

## Visualization

* Plotly

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

```text
.
├── app.py
├── generate_final_submission.py
├── rank_candidates.py
├── semantic_rerank.py
├── requirements.txt
├── submission_metadata.yaml
├── README.md
│
├── src/
│   ├── load_data.py
│   └── score_candidates.py
│
├── output/
│   └── final_submission.csv
│
├── screenshots/
│
└── validate_submission.py
```

---

# 📄 Output Format

The generated submission contains:

```text
candidate_id,rank,score,reasoning
```

### Columns

* **candidate_id** → Unique Candidate Identifier
* **rank** → Final Candidate Rank
* **score** → Normalized AI Ranking Score
* **reasoning** → Explainable AI Justification

---

# 🚀 Key Highlights

* Hybrid AI Ranking Engine
* Explainable AI
* Multi-Signal Candidate Evaluation
* Behavioral Intelligence
* AI Skill Matching
* Career Analysis
* Product Company Recognition
* Interactive Dashboard
* Streamlit Deployment
* Top 100 Candidate Recommendation

---

# 📸 Dashboard Preview

Include screenshots from the **screenshots/** folder.

Suggested order:

* Dashboard Overview
* Top 100 Rankings
* Candidate Explorer
* Explainable AI Decision
* Analytics Dashboard

---

# 🌐 Repository

GitHub Repository:

https://github.com/Tanmaisutrave/IndiaRuns-AI-Challenge

---

# 👨‍💻 Author

**Sutrave Tanmai**

B.Tech – Computer Science Engineering

MLR Institute of Technology

---

# 📜 License

Developed for the **India Runs Data & AI Challenge 2026**.

This repository is intended for educational and hackathon submission purposes.
