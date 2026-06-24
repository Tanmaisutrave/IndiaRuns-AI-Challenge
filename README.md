# AI Candidate Discovery & Ranking System

## Overview

This project was developed for the India Runs Data & AI Challenge.

The objective is to identify and rank the top 100 candidates from a dataset of 100,000 profiles for a specialized AI/ML role.

## Approach

### Feature Engineering

* Experience Score
* AI Skill Matching
* Career History Analysis
* Behavioral Signal Analysis
* Product Company Experience

### Behavioral Signals Used

* Recruiter Response Rate
* Interview Completion Rate
* Profile Completeness
* Open To Work Status
* Notice Period

### AI Skills Considered

* Embeddings
* Vector Search
* RAG
* Milvus
* FAISS
* Qdrant
* Fine-tuning LLMs
* Recommendation Systems
* Semantic Search

## Output

The system generates:

candidate_id, rank, score, reasoning

for the top 100 ranked candidates.

## Dashboard

Built using Streamlit.

Features:

* Candidate Ranking Table
* Candidate Profile Viewer
* Explainable AI
* Analytics Dashboard

## Technologies

* Python
* Pandas
* Streamlit
* Plotly
* Sentence Transformers
