import streamlit as st

st.title("🎓 Student Project Evaluator")
st.write("Enter your project details below")
project_title = st.text_input("Project Title")
project_description = st.text_area("Project Description")
technologies = st.text_input("Technologies Used")
if st.button("Evaluate Project"):
    st.subheader("📊 Evaluation Results")
    st.write("Score: 75 / 100")
    st.write("### Strengths")
st.write("- Clear project idea")

st.write("### Improvements")
st.write("- Add more technical details")
