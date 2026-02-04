import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# -------- Imports --------
import streamlit as st
from ml.evaluator import evaluate_project

# -------- Page Config --------
st.set_page_config(page_title="Student Project Evaluator", layout="centered")

# -------- UI --------
st.title("🎓 AI-Powered Student Project Evaluator")
st.write("Enter your project details to get an automated evaluation.")

# -------- Inputs --------
project_title = st.text_input("📌 Project Title")

project_description = st.text_area(
    "📝 Project Description",
    height=200
)

technologies = st.text_input(
    "🛠 Technologies Used (comma separated)"
)

# -------- Button Logic --------
if st.button("Evaluate Project"):

    if project_title and project_description and technologies:

        score, strengths, improvements = evaluate_project(
            project_title,
            project_description,
            technologies
        )

        st.divider()
        st.subheader("📊 Evaluation Results")

        st.metric("Final Score", f"{score}/100")

        st.write("### ✅ Strengths")
        if strengths:
            for s in strengths:
                st.write("•", s)
        else:
            st.write("No major strengths detected.")

        st.write("### ❌ Improvements")
        if improvements:
            for i in improvements:
                st.write("•", i)
        else:
            st.write("No major improvements required.")

    else:
        st.warning("⚠️ Please fill all fields before evaluation.")