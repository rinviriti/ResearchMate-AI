import google.generativeai as genai


def run_summary_agent(paper_text):
    prompt = f"""
You are the Summary Agent.

Your task is to summarize the research paper for a beginner researcher.

Include:
- Research problem
- Main objective
- Proposed method
- Key findings
- Main contribution

Paper text:
{paper_text[:12000]}
"""

    model = genai.GenerativeModel("gemini-3.5-flash")
    response = model.generate_content(prompt)
    return response.text