from agents.llm_utils import call_gemini, trim_text


def run_coordinator_agent(paper_text, paper_name="Uploaded Paper"):
    paper_text = trim_text(paper_text, 12000)

    prompt = f"""
You are the Coordinator Agent of ResearchMate AI.

Your job is to inspect the uploaded research paper and create a structured analysis plan for the downstream agents.

Paper name:
{paper_name}

Paper text:
{paper_text}

Return a professional coordinator analysis with:

## Paper Identification
- Probable title
- Research domain
- Paper type
- Main research problem
- Main contribution

## Detected Research Elements
- Dataset or data source
- Methods or algorithms
- Evaluation metrics
- Baselines or comparison methods
- Application area

## Recommended Agent Focus
Explain what each agent should focus on:
- Summary Agent
- Methodology Agent
- Evaluation Agent
- Research Gap Agent
- Research Mentor Agent
- Safety Review Agent

## Risk Flags
Mention if the paper involves medical, clinical, legal, financial, or other high-stakes claims.

## Confidence Level
Give confidence as High / Medium / Low with a short reason.

Important:
- Do not invent details.
- If something is not mentioned, write "Not clearly specified".
- Keep it structured and useful for other agents.
"""

    return call_gemini(prompt, temperature=0.2)


coordinator_agent = run_coordinator_agent