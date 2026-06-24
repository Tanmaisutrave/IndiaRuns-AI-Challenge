
AI_SKILLS = {
    "NLP",
    "Fine-tuning LLMs",
    "LoRA",
    "Milvus",
    "Transformers",
    "Embeddings",
    "Vector Search",
    "RAG",
    "PyTorch",
    "TensorFlow",
    "Machine Learning",
    "Deep Learning"
}

AI_TITLES = {
    "AI Engineer",
    "ML Engineer",
    "Machine Learning Engineer",
    "Applied Scientist",
    "NLP Engineer",
    "Research Engineer",
    "Data Scientist",
    "Search Engineer",
    "Recommendation Systems Engineer",
    "Senior AI Engineer",
    "Staff Machine Learning Engineer"
}

CAREER_KEYWORDS = {
    "ranking",
    "learning-to-rank",
    "retrieval",
    "search",
    "semantic search",
    "vector search",
    "embedding",
    "recommendation",
    "rag",
    "llm",
    "fine-tuning",
    "evaluation",
    "relevance",
    "bm25",
    "ndcg",
    "mrr",
    "map",
    "a/b testing"
}

PRODUCT_COMPANIES = {
    "Razorpay",
    "Zoho",
    "PharmEasy",
    "Freshworks",
    "Swiggy",
    "Flipkart",
    "Paytm",
    "Meesho"
}


def career_history_score(candidate):

    score = 0

    for job in candidate["career_history"]:

        text = (
            job["title"] + " " +
            job["description"]
        ).lower()

        for keyword in CAREER_KEYWORDS:

            if keyword in text:
                score += 3

    return min(score, 30)


def product_company_score(candidate):

    score = 0

    for job in candidate["career_history"]:

        if job["company"] in PRODUCT_COMPANIES:
            score += 5

    return min(score, 15)


def signal_score(candidate):

    signals = candidate["redrob_signals"]

    score = 0

    # Recruiter engagement
    score += signals["recruiter_response_rate"] * 10

    # Reliability
    score += signals["interview_completion_rate"] * 10

    # Recruiter interest
    score += min(
        signals["saved_by_recruiters_30d"] / 5,
        10
    )

    # Profile quality
    score += min(
        signals["profile_completeness_score"] / 10,
        10
    )

    # Open to work bonus
    if signals["open_to_work_flag"]:
        score += 5

    # Notice period bonus
    if signals["notice_period_days"] <= 30:
        score += 5

    elif signals["notice_period_days"] <= 60:
        score += 3

    return score


def calculate_score(candidate):

    score = 0

    # -----------------------
    # Experience
    # -----------------------

    exp = candidate["profile"]["years_of_experience"]

    if 5 <= exp <= 9:
        score += 25

    elif 3 <= exp <= 12:
        score += 15

    # -----------------------
    # Skills
    # -----------------------

    skills = {
        s["name"]
        for s in candidate["skills"]
    }

    matched = len(
        skills.intersection(AI_SKILLS)
    )

    score += matched * 5

    # -----------------------
    # Title
    # -----------------------

    title = candidate["profile"]["current_title"]

    if title in AI_TITLES:
        score += 20

    # -----------------------
    # GitHub
    # -----------------------

    github = candidate["redrob_signals"]["github_activity_score"]

    if github > 70:
        score += 15

    elif github > 40:
        score += 10

    # -----------------------
    # Career History
    # -----------------------

    score += career_history_score(candidate)

    # -----------------------
    # Behavioral Signals
    # -----------------------

    score += signal_score(candidate)

    # -----------------------
    # Product Companies
    # -----------------------

    score += product_company_score(candidate)

    return round(score, 2)

