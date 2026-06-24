# 🚀 AI Candidate Discovery & Ranking System

## India Runs Data & AI Challenge 2026

An Explainable AI-powered candidate ranking system designed to identify and rank the top 100 AI/ML candidates from a dataset of 100,000 candidate profiles.


## 📌 Problem Statement

The objective of this challenge is to discover and rank the most relevant candidates for a specialized AI/ML role using candidate profiles, career history, skills, and behavioral signals.

The final output consists of the top 100 ranked candidates along with transparent reasoning explaining why each candidate was selected.


## 🎯 Solution Overview

This project implements a Hybrid AI Ranking Engine that combines:

* AI/ML Skill Matching
* Experience Evaluation
* Career History Analysis
* Behavioral Signal Scoring
* Product Company Experience
* Explainable AI Reasoning

The ranking system generates a final score for every candidate and selects the top 100 profiles.


## 🧠 Ranking Methodology

### 1. Experience Scoring

Candidates are evaluated based on years of relevant professional experience.

### 2. AI Skill Matching

The system identifies high-value AI/ML skills including:

* Embeddings
* Vector Search
* RAG
* FAISS
* Milvus
* Qdrant
* Semantic Search
* Recommendation Systems
* Fine-tuning LLMs
* Deep Learning
* NLP
* Machine Learning

### 3. Career History Analysis

Past roles and project descriptions are analyzed for relevance to:

* Retrieval Systems
* Ranking Systems
* Search Applications
* Recommendation Engines
* LLM Applications

### 4. Behavioral Signal Analysis

The following Redrob behavioral signals are incorporated:

* Recruiter Response Rate
* Interview Completion Rate
* Profile Completeness Score
* Saved By Recruiters
* Open To Work Status
* Notice Period

### 5. Product Company Experience

Additional weight is assigned to candidates with experience in leading product-based organizations.


## 🤖 Explainable AI

For every ranked candidate, the system generates a human-readable explanation highlighting:

* Relevant AI skills
* Experience level
* Behavioral strengths
* Career relevance
* Ranking justification

This improves transparency and interpretability of the ranking process.


## 📊 Dashboard Features

A Streamlit-based dashboard was developed for visualization and analysis.

### Features

* Top 100 Candidate Rankings
* Candidate Explorer
* Explainable AI Insights
* Ranking Analytics Dashboard
* Score Distribution Analysis
* Rank vs Score Visualization
* Candidate Performance Metrics


## 🛠️ Technology Stack

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### AI / Machine Learning

* Sentence Transformers

### Visualization

* Plotly
* Streamlit

### Version Control

* Git
* GitHub


## 📂 Project Structure

```text
.
├── app.py
├── src/
│   ├── load_data.py
│   └── score_candidates.py
├── output/
│   └── final_submission.csv
├── screenshots/
├── requirements.txt
├── submission_metadata.yaml
└── README.md
```


## 📄 Output Format

The final submission contains:

```text
candidate_id, rank, score, reasoning
```

where:

* candidate_id → Candidate Identifier
* rank → Final Candidate Rank
* score → Normalized Ranking Score
* reasoning → Explainable Ranking Justification


## 🌐 Live Demo

Streamlit Dashboard:

https://indiaruns-ai-challenge-msyb6exnu7khfxetshkzgj.streamlit.app/


## 👨‍💻 Author

**Sutrave Tanmai**

B.Tech Computer Science Engineering
MLR Institute of Technology


## 📜 License

This project was developed for the India Runs Data & AI Challenge 2026.
