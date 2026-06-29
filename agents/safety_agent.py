from agents.llm_utils import call_gemini, trim_text


def run_safety_agent(
    summary,
    methodology,
    evaluation,
    future_work,
    research_gap="",
    scoring=""
):
    summary = trim_text(summary, 5000)
    methodology = trim_text(methodology, 5000)
    evaluation = trim_text(evaluation, 5000)
    future_work = trim_text(future_work, 5000)
    research_gap = trim_text(research_gap, 4000)
    scoring = trim_text(scoring, 4000)

    prompt = f"""
You are the Safety Review Agent of ResearchMate AI.

Review the AI-generated research analysis below.

SUMMARY:
{summary}

METHODOLOGY:
{methodology}

EVALUATION:
{evaluation}

FUTURE WORK / MENTOR:
{future_work}

RESEARCH GAP:
{research_gap}

SCORING:
{scoring}

Check whether the generated analysis:
- Makes unsupported claims
- Gives medical diagnosis or treatment advice
- Overstates research findings
- Presents speculation as fact
- Ignores limitations
- Lacks regulatory or human-review disclaimers
- Could mislead users in academic, clinical, legal, financial, or high-stakes contexts

Return the output in this structure:

## Safety Status
Safe / Needs Review / High Risk

## Issues Found
List specific safety or reliability issues.

## Overstated Claims
Identify statements that should be softened.

## Suggested Corrections
Rewrite risky statements in safer wording.

## Human-in-the-Loop Recommendation
Explain what type of human review is needed.

## Final Safety Note
Give a concise final warning or approval note.

Rules:
- Be strict for medical or clinical papers.
- Do not provide medical advice.
- Focus on safe wording and responsible AI use.
"""

    return call_gemini(prompt, temperature=0.2)