from agents.llm_utils import call_gemini, trim_text


def run_summary_agent(paper_text):
    paper_text = trim_text(paper_text, 14000)

    prompt = f"""
You are the Summary Agent of ResearchMate AI.

Summarize the research paper for a beginner researcher.

Paper text:
{paper_text}

Return the output in this structure:

## Overview
Briefly explain what the paper is about.

## Research Problem
Explain the problem the paper tries to solve.

## Main Objective
State the main objective of the study.

## Proposed Method
Explain the method, model, framework, or approach used.

## Key Findings
List the most important findings.

## Main Contribution
Explain what is new, useful, or important about the work.

## Beginner-Friendly Explanation
Explain the paper in simple language for a student.

Rules:
- Do not hallucinate.
- If details are missing, say "Not clearly specified".
- Avoid medical or clinical advice.
"""

    return call_gemini(prompt, temperature=0.3)