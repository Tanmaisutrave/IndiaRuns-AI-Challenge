from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.load_data import load_candidates
from src.score_candidates import calculate_score
import numpy as np

print("Loading candidates...")

candidates = load_candidates("candidates.jsonl")

print("Calculating baseline scores...")

ranked = []

for candidate in candidates:

    score = calculate_score(candidate)

    ranked.append({
        "candidate": candidate,
        "base_score": score
    })

ranked.sort(
    key=lambda x: x["base_score"],
    reverse=True
)

top_candidates = ranked[:500]

print("Loading embedding model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

jd_text = """
Senior AI Engineer

Build retrieval systems
Embeddings
Ranking systems
Recommendation systems
LLMs
Fine-tuning
Production ML
Search systems
Vector databases
Startup mindset
"""

jd_embedding = model.encode(
    jd_text,
    convert_to_numpy=True
)

print("Semantic reranking...")

results = []

for item in top_candidates:

    candidate = item["candidate"]

    profile = candidate["profile"]

    skills = " ".join(
        skill["name"]
        for skill in candidate["skills"]
    )

    history = " ".join(
        job["description"]
        for job in candidate["career_history"]
    )

    candidate_text = f"""
    {profile['headline']}
    {profile['summary']}
    {skills}
    {history}
    """

    candidate_embedding = model.encode(
        candidate_text,
        convert_to_numpy=True
    )

    semantic_score = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    final_score = (
        0.7 * item["base_score"]
        +
        30 * semantic_score
    )

    results.append({
        "candidate_id": candidate["candidate_id"],
        "name": profile["anonymized_name"],
        "title": profile["current_title"],
        "final_score": round(final_score, 2)
    })

results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)

print("\nTOP 20 AFTER SEMANTIC RERANKING\n")

for i, row in enumerate(results[:20], start=1):
    print(
        f"{i}. "
        f"{row['candidate_id']} | "
        f"{row['name']} | "
        f"{row['title']} | "
        f"{row['final_score']}"
    )