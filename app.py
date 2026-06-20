import streamlit as st
from PyPDF2 import PdfReader
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.subheader("Resume Content")

    st.text_area(
        "Extracted Text",
        text,
        height=300
    )

    skills = [
        "python",
        "java",
        "html",
        "css",
        "javascript",
        "mysql",
        "sql",
        "git",
        "github",
        "aws",
        "azure",
        "power bi",
        "excel",
        "php",
        "c++"
    ]

    found_skills = []

    for skill in skills:

        if skill in text.lower():

            found_skills.append(skill)

    st.subheader("📊 Resume Dashboard")

    ats_score = int(
        (len(found_skills) / len(skills)) * 100
    )

    missing_skills = []

    for skill in skills:

        if skill not in found_skills:

            missing_skills.append(skill)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{ats_score}/100"
        )

    with col2:
        st.metric(
            "Detected Skills",
            len(found_skills)
        )

    with col3:
        st.metric(
            "Missing Skills",
            len(missing_skills)
        )

    st.progress(ats_score)

    st.subheader("✅ Detected Skills")

    for skill in found_skills:

        st.success(skill.title())

    st.subheader("❌ Missing Skills")

    for skill in missing_skills:

        st.warning(skill.title())

    st.subheader("🏆 Resume Rating")

    if ats_score >= 80:

        st.success("Excellent Resume ⭐⭐⭐⭐⭐")

    elif ats_score >= 60:

        st.success("Good Resume ⭐⭐⭐⭐")

    elif ats_score >= 40:

        st.warning("Average Resume ⭐⭐⭐")

    else:

        st.error("Needs Improvement ⭐⭐")
    # ==========================
    # PIE CHART
    # ==========================

    st.subheader("📊 Skill Analytics")

    chart_data = pd.DataFrame(
        {
            "Category": ["Detected Skills", "Missing Skills"],
            "Count": [
                len(found_skills),
                len(missing_skills)
            ]
        }
    )

    fig = px.pie(
        chart_data,
        names="Category",
        values="Count",
        title="Skill Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("💡 Suggestions")

    if "git" not in found_skills:
        st.info("Learn Git and GitHub.")

    if "sql" not in found_skills:
        st.info("Add SQL skills.")

    if "aws" not in found_skills:
        st.info("Learn AWS Cloud.")

    if "power bi" not in found_skills:
        st.info("Learn Power BI for analytics.")