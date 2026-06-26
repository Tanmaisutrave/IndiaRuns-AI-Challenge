
from datetime import datetime

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
    "Deep Learning",
    "Semantic Search",
    "Recommendation Systems",
    "Learning to Rank",
    "BM25",
    "FAISS",
    "Qdrant",
    "Weaviate",
    "LangChain",
    "LlamaIndex",
    "OpenAI API",
    "BentoML",
    "Weights & Biases",
    "Apache Spark",
    "PySpark",
    "Spark",
    "Kafka",
    "MLOps",
    "Image Classification",
    "Speech Recognition",
    "GANs"
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
    "Staff Machine Learning Engineer",
    "AI Research Scientist",
    "Principal AI Engineer",
    "Lead ML Engineer",
    "Senior Applied Scientist",
    "AI Scientist",
    "Computer Vision Engineer",
    "MLOps Engineer",
    "Generative AI Engineer",
    "LLM Engineer"
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
    "a/b testing",
    "faiss",
    "qdrant",
    "milvus",
    "weaviate",
    "semantic retrieval",
    "vector database",
    "langchain",
    "llamaindex",
    "knowledge graph",
    "reranking",
    "cross encoder",
    "dense retrieval",
    "hybrid search",
    "contrastive learning"
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

AI_COMPANIES = {
    "OpenAI",
    "Google",
    "Microsoft",
    "Amazon",
    "Meta",
    "NVIDIA",
    "IBM",
    "Salesforce",
    "Adobe",
    "Oracle"
}


def career_history_score(candidate):

    score = 0
    career_history = candidate.get("career_history", [])

    for job in career_history:
        title = job.get("title", "").lower()
        company = job.get("company", "")
        description = job.get("description", "").lower()
        duration_months = job.get("duration_months", 0)
        text = f"{title} {description}"

        if "engineer" in title:
            score += 2

        if "scientist" in title:
            score += 3

        if duration_months >= 24:
            score += 2

        company_lower = company.lower()
        if company_lower in {c.lower() for c in PRODUCT_COMPANIES} or company_lower in {c.lower() for c in AI_COMPANIES}:
            score += 5

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

    signals = candidate.get("redrob_signals", {})
    score = 0

    score += min(signals.get("profile_completeness_score", 0) / 10, 10)
    score += min(signals.get("profile_views_received_30d", 0) / 25, 5)
    score += min(signals.get("search_appearance_30d", 0) / 25, 10)
    score += min(signals.get("connection_count", 0) / 100, 5)
    score += min(signals.get("endorsements_received", 0) / 20, 5)
    score += min(signals.get("applications_submitted_30d", 0) / 5, 5)
    score += min(signals.get("saved_by_recruiters_30d", 0) / 5, 5)
    score += min(signals.get("interview_completion_rate", 0) * 10, 10)
    score += min(signals.get("recruiter_response_rate", 0) * 10, 10)

    avg_response_time = signals.get("avg_response_time_hours", 72)
    score += min(max((72 - avg_response_time) / 72 * 5, 0), 5)

    assessments = signals.get("skill_assessment_scores", {})
    if assessments:
        average_assessment = sum(assessments.values()) / len(assessments)
        score += min(average_assessment / 20, 5)

    offer_rate = signals.get("offer_acceptance_rate", -1)
    if offer_rate >= 0:
        score += min(offer_rate * 5, 5)

    score += 2 if signals.get("verified_email") else 0
    score += 2 if signals.get("verified_phone") else 0
    score += 1 if signals.get("linkedin_connected") else 0

    preferred_work_mode = signals.get("preferred_work_mode", "").lower()
    if preferred_work_mode in {"remote", "flexible"}:
        score += 3
    elif preferred_work_mode == "hybrid":
        score += 2
    elif preferred_work_mode == "onsite":
        score += 1

    if signals.get("willing_to_relocate"):
        score += 2

    open_to_work = signals.get("open_to_work_flag")
    if open_to_work:
        score += 3

    notice_period = signals.get("notice_period_days", 180)
    if notice_period <= 30:
        score += 3
    elif notice_period <= 60:
        score += 2

    last_active_date = signals.get("last_active_date")
    if last_active_date:
        try:
            last_active = datetime.fromisoformat(last_active_date)
            days_since_active = (datetime.now() - last_active).days
            if days_since_active <= 7:
                score += 4
            elif days_since_active <= 30:
                score += 2
        except ValueError:
            pass

    return min(score, 50)


def calculate_score(candidate):

    score = 0

    # -----------------------
    # Experience
    # -----------------------

    exp = candidate["profile"].get("years_of_experience", 0)

    if 5 <= exp <= 9:
        score += 25

    elif 3 <= exp <= 12:
        score += 15

    # -----------------------
    # Skills
    # -----------------------

    for skill in candidate.get("skills", []):

        if skill.get("name") not in AI_SKILLS:
            continue

        # Base match
        score += 4

        # Proficiency
        proficiency = skill.get("proficiency", "").lower()

        if proficiency == "expert":
            score += 4
        elif proficiency == "advanced":
            score += 3
        elif proficiency == "intermediate":
            score += 2
        else:
            score += 1

        # Endorsements
        score += min(
            skill.get("endorsements", 0) / 20,
            3
        )

        # Experience with skill
        score += min(
            skill.get("duration_months", 0) / 24,
            3
        )

        # Assessment scores
        assessments = candidate.get("redrob_signals", {}).get("skill_assessment_scores", {})

        if skill.get("name") in assessments:
            score += assessments[skill["name"]] / 25

    # -----------------------
    # Title
    # -----------------------

    title = candidate["profile"].get("current_title", "").lower()

    for ai_title in AI_TITLES:
        if ai_title.lower() in title:
            score += 15

    if "machine learning" in title:
        score += 3

    if "ai" in title and "machine learning" not in title:
        score += 3

    if "search" in title:
        score += 2

    if "recommendation" in title:
        score += 2

    # -----------------------
    # GitHub
    # -----------------------

    github = candidate.get("redrob_signals", {}).get("github_activity_score", 0)

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
    # Education
    # -----------------------

    score += education_score(candidate)

    # -----------------------
    # Product Companies
    # -----------------------

    score += product_company_score(candidate)

    return round(score, 2)


def education_score(candidate):
    score = 0
    education = candidate.get("education", [])

    for record in education:
        degree = record.get("degree", "").lower()
        field = record.get("field_of_study", "").lower()
        tier = record.get("tier", "unknown").lower()

        if any(keyword in degree for keyword in ["phd", "doctor", "masters", "m.s", "ms", "mtech", "mphil", "m.tech", "m.phil"]):
            score += 5
        elif any(keyword in degree for keyword in ["be", "btech", "bachelors", "bsc", "ba", "bs", "b.e", "b.tech"]):
            score += 3
        elif degree:
            score += 1

        if any(keyword in field for keyword in ["computer science", "machine learning", "artificial intelligence", "data science", "computer vision", "natural language", "nlp", "statistics", "electrical engineering"]):
            score += 3
        elif field:
            score += 1

        if tier == "tier_1":
            score += 2
        elif tier == "tier_2":
            score += 1

    return min(score, 10)

