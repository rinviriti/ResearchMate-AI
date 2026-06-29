from agents.llm_utils import call_gemini, trim_text


def run_research_mentor_agent(paper_text):
    paper_text = trim_text(paper_text, 14000)

    prompt = f"""
You are the Research Mentor Agent of ResearchMate AI.

Act like an academic mentor helping a student understand how to extend this paper.

Paper text:
{paper_text}

Return the output in this structure:

## Possible Improvements
Suggest realistic improvements to the study.

## Research Gaps
Identify important gaps that could become future work.

## New Experiment Ideas
Suggest experiments that can be implemented in future research.

## Dataset Improvement Ideas
Suggest how the dataset or data collection could be improved.

## Practical Application Ideas
Suggest possible real-world applications carefully.

## Recommended Next Step
Suggest one practical next step for a student researcher.

Rules:
- Be realistic and implementable.
- Do not claim something is clinically usable unless validated.
- For medical papers, include human expert review and validation warnings.
"""

    return call_gemini(prompt, temperature=0.4)