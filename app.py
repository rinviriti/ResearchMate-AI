import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

from utils.pdf_reader import extract_text_from_pdf
from agents.summary_agent import run_summary_agent
from agents.methodology_agent import run_methodology_agent
from agents.evaluation_agent import run_evaluation_agent
from agents.research_mentor_agent import run_research_mentor_agent
from agents.safety_agent import run_safety_agent


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)


st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ResearchMate AI")
st.subheader("A Multi-Agent Research Paper Assistant")

st.write(
    "Upload a research paper PDF and let multiple AI agents analyze its summary, "
    "methodology, evaluation, future work, and safety."
)

uploaded_file = st.file_uploader("Upload a research paper PDF", type=["pdf"])

if not api_key:
    st.error("Gemini API key not found. Please add GEMINI_API_KEY to your .env file.")

if uploaded_file is not None and api_key:
    with st.spinner("Extracting text from PDF..."):
        paper_text = extract_text_from_pdf(uploaded_file)

    if len(paper_text.strip()) == 0:
        st.error("No readable text found in this PDF.")
    else:
        st.success("PDF text extracted successfully.")

        with st.expander("Preview extracted text"):
            st.write(paper_text[:3000])

        if st.button("Run Multi-Agent Analysis"):
            with st.spinner("Summary Agent is analyzing the paper..."):
                summary = run_summary_agent(paper_text)

            with st.spinner("Methodology Agent is extracting methodology..."):
                methodology = run_methodology_agent(paper_text)

            with st.spinner("Evaluation Agent is analyzing results..."):
                evaluation = run_evaluation_agent(paper_text)

            with st.spinner("Research Mentor Agent is generating future work ideas..."):
                future_work = run_research_mentor_agent(paper_text)

            with st.spinner("Safety Review Agent is checking the outputs..."):
                safety_review = run_safety_agent(
                    summary,
                    methodology,
                    evaluation,
                    future_work
                )

            st.divider()

            st.header("🧠 Multi-Agent Analysis Results")

            tab1, tab2, tab3, tab4, tab5 = st.tabs(
                [
                    "Summary Agent",
                    "Methodology Agent",
                    "Evaluation Agent",
                    "Research Mentor Agent",
                    "Safety Review Agent"
                ]
            )

            with tab1:
                st.subheader("Summary")
                st.write(summary)

            with tab2:
                st.subheader("Methodology")
                st.write(methodology)

            with tab3:
                st.subheader("Evaluation")
                st.write(evaluation)

            with tab4:
                st.subheader("Future Research Ideas")
                st.write(future_work)

            with tab5:
                st.subheader("Safety Review")
                st.write(safety_review)

            st.divider()

            st.info(
                "Human-in-the-loop reminder: AI-generated research analysis should be reviewed "
                "by a human researcher before being used in academic or clinical decisions."
            )

else:
    st.info("Please upload a PDF paper to begin.")