import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import streamlit as st
from ml.evaluator import evaluate_project
st.set_page_config(
    page_title="Student Project Evaluator",
    layout="centered"
)

st.title("🎓 AI-Based Student Project Evaluator")
st.write(
    "This tool evaluates student projects based on **innovation**, "
    "**real-world impact**, and **technical depth**."
)

# -------- Input Section --------
st.subheader("📌 Enter Project Details")

title = st.text_input("Project Title")
description = st.text_area("Project Description", height=220)
technologies = st.text_input("Technologies / Tools Used")

# -------- Evaluation --------
if st.button("Evaluate Project"):
    if not title or not description or not technologies:
        st.warning("⚠️ Please fill in all the fields before evaluation.")
    else:
        score, strengths, improvements, suitability = evaluate_project(
            title, description, technologies
        )

        st.divider()

        # -------- Score --------
        st.subheader("📊 Evaluation Score")
        st.metric(label="Overall Score", value=f"{score}/100")

        # -------- Suitability --------
        st.subheader("🌍 Real-World Suitability")
        if score >= 75:
            st.success(suitability)
        elif score >= 50:
            st.warning(suitability)
        else:
            st.error(suitability)

        # -------- Strengths --------
        if strengths:
            st.subheader("✅ Strengths Identified")
            for s in strengths:
                st.write("•", s)

        # -------- Improvements --------
        if improvements:
            st.subheader("⚠️ Areas Needing Improvement")
            for i in improvements:
                st.write("•", i)

        st.divider()
        st.caption("🔍 Evaluation is based on rule-based NLP analysis")

