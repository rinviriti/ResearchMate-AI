import google.generativeai as genai


def run_methodology_agent(paper_text):
    prompt = f"""
You are the Methodology Agent.

Extract the methodology from the paper.

Focus on:
- Dataset
- Preprocessing
- Model or algorithm
- Training process
- Experimental setup
- Tools or frameworks

Paper text:
{paper_text[:12000]}
"""

    model = genai.GenerativeModel("gemini-3.5-flash")
    response = model.generate_content(prompt)
    return response.text