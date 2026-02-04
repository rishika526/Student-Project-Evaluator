from ml.preprocess import clean_text
from ml.keyword import TECH_KEYWORDS

def evaluate_project(title, description, technologies):
    score = 0
    strengths = []
    improvements = []

    full_text = clean_text(title + " " + description + " " + technologies)

    # Description quality
    if len(description.split()) >= 50:
        score += 30
        strengths.append("Well detailed project description")
    else:
        improvements.append("Add more details to project description")

    # Technical relevance
    keywords_count = 0
    for keyword in TECH_KEYWORDS:
        if keyword in full_text:
            keywords_count += 1

    score += min(keywords_count * 5, 30)

    # Title clarity
    if len(title.split()) >= 3:
        score += 20
        strengths.append("Clear and descriptive project title")
    else:
        improvements.append("Need a clearer project title")

    score = min(score, 100)
    return score, strengths, improvements


if __name__ == "__main__":
    result = evaluate_project(
        "AI Attendance System",
        "This project uses machine learning to automate attendance using facial recognition and image processing techniques.",
        "Python, Machine Learning, OpenCV"
    )
    print(result)
