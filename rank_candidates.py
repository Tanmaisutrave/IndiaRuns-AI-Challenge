from src.load_data import load_candidates
from src.score_candidates import calculate_score

print("Loading candidates...")

candidates = load_candidates("candidates.jsonl")

print("Scoring candidates...")

ranked = []

for candidate in candidates:
    score = calculate_score(candidate)

    ranked.append({
        "candidate_id": candidate["candidate_id"],
        "name": candidate["profile"]["anonymized_name"],
        "title": candidate["profile"]["current_title"],
        "score": score
    })

ranked.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 20 CANDIDATES\n")

for i, candidate in enumerate(ranked[:20], start=1):
    print(
        f"{i}. "
        f"{candidate['candidate_id']} | "
        f"{candidate['name']} | "
        f"{candidate['title']} | "
        f"Score = {candidate['score']}"
    )