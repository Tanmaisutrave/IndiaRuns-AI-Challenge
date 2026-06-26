from src.constants import *


# ==========================================
# EXPERIENCE SCORE
# Max Score = 20
# ==========================================

def experience_score(candidate):

    exp = candidate["profile"]["years_of_experience"]

    if 5 <= exp <= 8:
        return 20

    elif 3 <= exp < 5:
        return 16

    elif 8 < exp <= 12:
        return 15

    elif 1 <= exp < 3:
        return 8

    else:
        return 3
    
# ==========================================
# TITLE SCORE
# Max Score = 20
# ==========================================

def title_score(candidate):

    title = candidate["profile"]["current_title"].lower()

    score = 0

    for ai_title in AI_TITLES:

        if ai_title.lower() in title:
            score += 15

    # Additional keyword boosts
    if "ai" in title:
        score += 3

    if "machine learning" in title:
        score += 3

    if "search" in title:
        score += 2

    if "recommendation" in title:
        score += 2

    return min(score, 20)

# ==========================================
# GITHUB SCORE
# Max Score = 10
# ==========================================

def github_score(candidate):

    github = candidate["redrob_signals"]["github_activity_score"]

    if github < 0:
        return 0

    elif github >= 90:
        return 10

    elif github >= 70:
        return 8

    elif github >= 50:
        return 6

    elif github >= 30:
        return 4

    return 2

# ==========================================
# SKILL SCORE
# Max Score = 40
# ==========================================

def skill_score(candidate):

    score = 0

    for skill in candidate["skills"]:

        name = skill.get("name", "")

        if name not in AI_SKILLS:
            continue

        # --------------------------------
        # Base Skill Match
        # --------------------------------

        score += 4

        # --------------------------------
        # Proficiency
        # --------------------------------

        proficiency = skill.get("proficiency", "").lower()

        if proficiency == "expert":
            score += 4

        elif proficiency == "advanced":
            score += 3

        elif proficiency == "intermediate":
            score += 2

        elif proficiency == "beginner":
            score += 1

        # --------------------------------
        # Endorsements
        # --------------------------------

        endorsements = skill.get("endorsements", 0)

        if endorsements >= 100:
            score += 5

        elif endorsements >= 50:
            score += 4

        elif endorsements >= 20:
            score += 3

        elif endorsements >= 10:
            score += 2

        elif endorsements > 0:
            score += 1

        # --------------------------------
        # Experience with Skill
        # --------------------------------

        months = skill.get("duration_months", 0)

        if months >= 60:
            score += 5

        elif months >= 36:
            score += 4

        elif months >= 24:
            score += 3

        elif months >= 12:
            score += 2

        elif months > 0:
            score += 1

    return min(score, 40)