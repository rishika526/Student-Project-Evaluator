from ml.preprocess import clean_text
from ml.keyword import COMMON_PROJECTS, REAL_WORLD_KEYWORDS, ML_KEYWORDS

def evaluate_project(title, description, technologies):
    score = 0
    strengths = []
    improvements = []

    full_text = clean_text(title + " " + description + " " + technologies)

    # 1️⃣ UNIQUENESS (40)
    uniqueness_score = 40
    for project in COMMON_PROJECTS:
        if project in full_text:
            uniqueness_score -= 10

    uniqueness_score = max(uniqueness_score, 10)
    score += uniqueness_score

    if uniqueness_score >= 30:
        strengths.append("Project idea demonstrates innovation.")
    else:
        improvements.append(
            "Project idea is common. Introduce a novel feature or target a new domain."
        )

    # 2️⃣ REAL-WORLD IMPACT (40)
    impact_matches = sum(1 for k in REAL_WORLD_KEYWORDS if k in full_text)

    if impact_matches >= 2:
        impact_score = 40
    elif impact_matches == 1:
        impact_score = 25
    else:
        impact_score = 10

    score += impact_score

    if impact_score >= 30:
        strengths.append("Strong real-world relevance and practical use case.")
    else:
        improvements.append(
            "Real-world impact is limited. Clearly explain who benefits and how it will be used."
        )

    # 3️⃣ TECHNICAL DEPTH (20)
    ml_matches = sum(1 for k in ML_KEYWORDS if k in full_text)

    if ml_matches >= 2:
        tech_score = 20
    elif ml_matches == 1:
        tech_score = 12
    else:
        tech_score = 5

    score += tech_score

    if tech_score >= 15:
        strengths.append("Good technical and ML depth.")
    else:
        improvements.append(
            "Technical depth is low. Include ML model details, training process, and evaluation."
        )

    score = min(score, 100)

    # 🌍 REAL-WORLD SUITABILITY
    if score >= 75:
        suitability = "Highly suitable for real-world deployment"
    elif score >= 50:
        suitability = "Moderately suitable with improvements"
    else:
        suitability = "Not suitable for real-world deployment"

    return score, strengths, improvements, suitability
