import pandas as pd

from src.load_data import load_candidates
from src.score_candidates import calculate_score

def generate_reasoning(candidate):

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    JD_SKILLS = {
        "Embeddings",
        "Vector Search",
        "RAG",
        "Milvus",
        "Qdrant",
        "FAISS",
        "BM25",
        "Learning to Rank",
        "Recommendation Systems",
        "Semantic Search",
        "Fine-tuning LLMs"
    }

    matched_skills = [
        s["name"]
        for s in candidate["skills"]
        if s["name"] in JD_SKILLS
    ]

    if len(matched_skills) >= 3:
        top_skills = ", ".join(matched_skills[:3])

        skill_text = (
            f"Strong match for retrieval and ranking systems through "
            f"{top_skills} experience."
        )

    elif len(matched_skills) > 0:
        top_skills = ", ".join(matched_skills)

        skill_text = (
            f"Relevant AI experience in {top_skills}."
        )

    else:
        skill_text = (
            "Relevant machine learning and production AI experience."
        )

    return (
        f"{profile['current_title']} with "
        f"{profile['years_of_experience']} years experience. "
        f"{skill_text} "
        f"High recruiter engagement "
        f"({signals['recruiter_response_rate']:.2f} response rate) "
        f"and strong interview reliability "
        f"({signals['interview_completion_rate']:.2f} completion rate)."
    )

print("Loading candidates...")

candidates = load_candidates("candidates.jsonl")

print("Scoring candidates...")

ranked = []

for candidate in candidates:

    score = calculate_score(candidate)

    ranked.append({
        "candidate": candidate,
        "score": score
    })

ranked.sort(
    key=lambda x: x["score"],
    reverse=True
)


top_100 = ranked[:100]


max_score = top_100[0]["score"]
min_score = top_100[-1]["score"]

rows = []

for rank, item in enumerate(top_100, start=1):

    candidate = item["candidate"]
    score = item["score"]

    normalized_score = (
        (score - min_score)
        /
        (max_score - min_score)
    )

    rows.append({
        "candidate_id": candidate["candidate_id"],
        "rank": rank,
        "score": round(normalized_score, 4),
        "reasoning": generate_reasoning(candidate)
    })


df = pd.DataFrame(rows)

df.to_csv(
    "output/final_submission.csv",
    index=False
)

print("\nSaved:")
print("output/final_submission.csv")
print("\nRows:", len(df))

