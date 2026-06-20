import google.generativeai as genai


def run_research_mentor_agent(paper_text):
    prompt = f"""
You are the Research Mentor Agent.

Based on the paper, suggest future research directions.

Include:
- Possible improvements
- Research gaps
- New experiment ideas
- Dataset improvement ideas
- Practical application ideas

Paper text:
{paper_text[:12000]}
"""

    model = genai.GenerativeModel("gemini-3.5-flash")
    response = model.generate_content(prompt)
    return response.text