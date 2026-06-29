from agents.llm_utils import call_gemini, trim_text


def run_research_gap_agent(paper_text, mentor_text="", evaluation_text=""):
    paper_text = trim_text(paper_text, 12000)
    mentor_text = trim_text(mentor_text, 5000)
    evaluation_text = trim_text(evaluation_text, 5000)

    prompt = f"""
You are the Research Gap Agent of ResearchMate AI.

Your task is to identify meaningful research gaps from the paper and previous agent outputs.

Paper text:
{paper_text}

Evaluation Agent Output:
{evaluation_text}

Research Mentor Agent Output:
{mentor_text}

Return the output in this structure:

## Explicit Research Gaps
List gaps directly mentioned by the paper.

## Hidden Research Gaps
List gaps that can be reasonably inferred from the methodology, evaluation, or limitations.

## Dataset Gaps
Mention missing data diversity, size, external validation, demographics, or domain coverage.

## Methodology Gaps
Mention missing ablation, explainability, comparison, robustness, or reproducibility issues.

## Practical Deployment Gaps
Mention real-world testing, clinical validation, usability, regulation, scalability, or safety concerns.

## Top 5 Future Research Opportunities
Give five clear future research directions.

Rules:
- Do not exaggerate.
- Clearly distinguish between paper-stated gaps and inferred gaps.
- Avoid giving clinical treatment advice.
"""

    return call_gemini(prompt, temperature=0.35)


research_gap_agent = run_research_gap_agent