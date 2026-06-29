from agents.llm_utils import call_gemini, trim_text


def run_evaluation_agent(paper_text):
    paper_text = trim_text(paper_text, 14000)

    prompt = f"""
You are the Evaluation Agent of ResearchMate AI.

Analyze how the paper evaluates its work.

Paper text:
{paper_text}

Return the output in this structure:

## Evaluation Metrics
List the metrics used in the paper.

## Baseline Methods
Identify baseline or comparison methods.

## Main Results
Summarize the reported results.

## Comparative Performance
Explain whether the proposed method performs better, worse, or similarly compared to baselines.

## Strengths of Evaluation
Mention strong points in the evaluation design.

## Limitations of Evaluation
Mention weaknesses, missing comparisons, small datasets, lack of validation, or incomplete reporting.

## Overall Evaluation Quality
Rate the evaluation quality as High / Medium / Low with reasons.

Rules:
- Do not invent numbers.
- If metrics are missing, say so clearly.
- Keep the tone objective.
"""

    return call_gemini(prompt, temperature=0.25)