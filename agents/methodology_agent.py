from agents.llm_utils import call_gemini, trim_text


def run_methodology_agent(paper_text):
    paper_text = trim_text(paper_text, 14000)

    prompt = f"""
You are the Methodology Agent of ResearchMate AI.

Analyze the methodology of the paper.

Paper text:
{paper_text}

Return the output in this structure:

## Dataset / Data Source
Mention dataset name, source, size, or cohort if available.

## Preprocessing
Identify cleaning, normalization, augmentation, feature extraction, or preparation steps.

## Model / Algorithm / Method
Explain the main method, model, algorithm, framework, or statistical technique.

## Experimental Setup
Describe training, testing, validation, comparison setup, or study design.

## Tools / Frameworks
Mention software, libraries, platforms, or statistical tools if specified.

## Reproducibility Notes
Explain whether the methodology has enough detail to reproduce the study.

## Missing Methodological Details
List any important missing details.

Rules:
- Do not invent tools, datasets, or preprocessing.
- If not specified, clearly say "Not specified in the paper".
- Be precise and academic.
"""

    return call_gemini(prompt, temperature=0.25)