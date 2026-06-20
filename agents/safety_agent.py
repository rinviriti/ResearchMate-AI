import google.generativeai as genai


def run_safety_agent(summary, methodology, evaluation, future_work):
    prompt = f"""
You are the Safety Review Agent.

Review the following AI-generated research analysis.

Check whether the output:
- Makes unsupported claims
- Gives medical diagnosis or treatment advice
- Overstates findings
- Uses unsafe language
- Presents speculation as fact

Return:
1. Safety status: Safe / Needs Review
2. Issues found
3. Suggested corrections
4. Final safety note

Generated analysis:

SUMMARY:
{summary}

METHODOLOGY:
{methodology}

EVALUATION:
{evaluation}

FUTURE WORK:
{future_work}
"""

    model = genai.GenerativeModel("gemini-3.5-flash")
    response = model.generate_content(prompt)
    return response.text