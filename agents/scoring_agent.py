from agents.llm_utils import call_gemini, trim_text


def run_scoring_agent(
    coordinator,
    summary,
    methodology,
    evaluation,
    mentor,
    research_gap
):
    coordinator = trim_text(coordinator, 4000)
    summary = trim_text(summary, 4000)
    methodology = trim_text(methodology, 4000)
    evaluation = trim_text(evaluation, 4000)
    mentor = trim_text(mentor, 4000)
    research_gap = trim_text(research_gap, 4000)

    prompt = f"""
You are the Scoring Agent of ResearchMate AI.

Evaluate the research paper based on the outputs from previous agents.

Coordinator:
{coordinator}

Summary:
{summary}

Methodology:
{methodology}

Evaluation:
{evaluation}

Research Mentor:
{mentor}

Research Gap:
{research_gap}

Return a professional scorecard.

Use this exact structure:

## Research Assessment Scores

| Metric | Score | Reason |
|---|---:|---|
| Research Quality | X/10 | Reason |
| Novelty | X/10 | Reason |
| Methodology Clarity | X/10 | Reason |
| Evaluation Strength | X/10 | Reason |
| Reproducibility | X/10 | Reason |
| Practical Relevance | X/10 | Reason |
| Safety Awareness | X/10 | Reason |

## Overall Score
Give an overall score out of 10.

## Score Justification
Explain the score in one short paragraph.

Rules:
- Scores must be justified.
- Do not give perfect scores unless strongly supported.
- Penalize missing methodology, missing dataset details, weak evaluation, or unsupported claims.
"""

    return call_gemini(prompt, temperature=0.25)


scoring_agent = run_scoring_agent