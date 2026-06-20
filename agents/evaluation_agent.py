import google.generativeai as genai


def run_evaluation_agent(paper_text):
    prompt = f"""
You are the Evaluation Agent.

Analyze the evaluation section of the paper.

Extract:
- Evaluation metrics
- Baseline methods
- Results
- Comparisons
- Limitations

Paper text:
{paper_text[:12000]}
"""

    model = genai.GenerativeModel("gemini-3.5-flash")
    response = model.generate_content(prompt)
    return response.text