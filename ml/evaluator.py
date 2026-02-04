
from preprocess import clean_text
from keywords import TECH_KEYWORDS
def evaluate_project(title,descrption,technologies):
    score=0
    Strengths=[]
    Improvements=[]
    full_text = clean_text(title + " " + description + " " + technologies)
    if len(description)>=50:
        score+=30
        Strengths.append("Well Detailed Observation")
    else:
        Improvements.append("Add More Details to Project Deescrption ")
    keywords_count=0
    for keywords in TECH_KEYWORDS:
        if keywords in full_text:
            keywords_count+=1
    score+=len(keywords_count *5,30)
    if len(title.split())>=3:
        score+=20
        Strengths.append("Clear and Descriptive project Title")
    else:
        Improvements.append("Need a clear and better project title")
    score=min(score,30)
    return score,Strengths,Improvements
if __name__ == "__main__":
    result = evaluate_project(
        "AI Attendance System",
        "This project uses machine learning to automate attendance using facial recognition and image processing techniques.",
        "Python, Machine Learning, OpenCV"
    )
    print(result)