from agents.llm_utils import call_gemini, trim_text


def run_final_verdict_agent(
    coordinator,
    summary,
    methodology,
    evaluation,
    research_gap,
    mentor,
    scoring,
    safety
):
    coordinator = trim_text(coordinator, 3500)
    summary = trim_text(summary, 3500)
    methodology = trim_text(methodology, 3500)
    evaluation = trim_text(evaluation, 3500)
    research_gap = trim_text(research_gap, 3500)
    mentor = trim_text(mentor, 3500)
    scoring = trim_text(scoring, 3500)
    safety = trim_text(safety, 3500)

    prompt = f"""
You are the Final Verdict Agent of ResearchMate AI.

Your task is to synthesize all agent outputs into a final professional judgment.

Coordinator:
{coordinator}

Summary:
{summary}

Methodology:
{methodology}

Evaluation:
{evaluation}

Research Gap:
{research_gap}

Mentor:
{mentor}

Scoring:
{scoring}

Safety:
{safety}

Return the output in this structure:

## Final Verdict

## Overall Recommendation
State whether the paper is useful for:
- Literature review
- Thesis background
- Methodology reference
- Practical deployment
- Future research

## Main Strengths
List the strongest aspects of the paper.

## Main Weaknesses
List important weaknesses or limitations.

## Best Use Case
Explain how students or researchers should use this paper.

## Risk Level
Low / Medium / High, with reason.

## Final Recommendation
Give a concise final recommendation.

Rules:
- Do not simply repeat previous outputs.
- Synthesize.
- Be balanced.
- For medical or clinical research, clearly state that clinical use requires expert validation.
"""

    return call_gemini(prompt, temperature=0.25)


final_verdict_agent = run_final_verdict_agent