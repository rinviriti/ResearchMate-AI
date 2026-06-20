# 📚 ResearchMate AI

## A Multi-Agent Research Paper Assistant

ResearchMate AI is an intelligent multi-agent system designed to help students, researchers, and academics analyze scientific research papers automatically.

The platform extracts text from uploaded PDF papers and coordinates multiple specialized AI agents to generate comprehensive insights including summaries, methodology explanations, evaluation reports, future research directions, and safety reviews.

Built as a capstone project for the **Google × Kaggle 5-Day AI Agents: Intensive Vibe Coding Course 2026**.

---

## 🚀 Features

### 📄 PDF Research Paper Analysis

* Upload any academic research paper in PDF format
* Automatic text extraction
* Support for large research documents

### 🤖 Multi-Agent Architecture

ResearchMate AI uses five specialized AI agents:

| Agent                 | Responsibility                                             |
| --------------------- | ---------------------------------------------------------- |
| Summary Agent         | Generates beginner-friendly summaries                      |
| Methodology Agent     | Explains research methods and workflows                    |
| Evaluation Agent      | Reviews strengths, weaknesses, and limitations             |
| Research Mentor Agent | Suggests future research directions and project ideas      |
| Safety Review Agent   | Detects risks, speculative claims, and missing disclaimers |

---

## 🧠 Agent Workflow

```text
Research Paper PDF
        │
        ▼
Text Extraction Layer
        │
        ▼
┌─────────────────────┐
│ Summary Agent       │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Methodology Agent   │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Evaluation Agent    │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Research Mentor     │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Safety Review Agent │
└─────────────────────┘
        │
        ▼
Comprehensive Analysis Report
```

---

## 🛡️ Safety & Human-in-the-Loop Review

ResearchMate AI includes a dedicated Safety Review Agent that evaluates generated content for:

* Medical misinformation risks
* Overstated conclusions
* Unsupported claims
* Missing disclaimers
* Hallucination-prone recommendations

This provides a human-in-the-loop review layer for high-stakes domains such as healthcare and biomedical research.

---

## 📸 Screenshots

### Dashboard

Upload a research paper and launch multi-agent analysis.

![Main Dashboard](Screenshots/Dashboard.png)

---

### Summary Agent

Generates beginner-friendly summaries and explains the research problem.

![Summary Agent](Screenshots/Summary Agent.png)

---

### Safety Review Agent

Performs safety evaluation and highlights potential risks.

![Safety Review Agent](Screenshots/Safety Review Agent.png)

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini API

### PDF Processing

* PyPDF2

### Development Tools

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
ResearchMate-AI/
│
├── agents/
│   ├── summary_agent.py
│   ├── methodology_agent.py
│   ├── evaluation_agent.py
│   ├── research_mentor_agent.py
│   └── safety_agent.py
│
├── skills/
│   ├── summary_skill.md
│   ├── methodology_skill.md
│   ├── evaluation_skill.md
│   ├── research_mentor_skill.md
│   └── safety_skill.md
│
├── utils/
│   └── pdf_reader.py
│
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/rinviriti/ResearchMate-AI.git
cd ResearchMate-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## 💡 Example Use Cases

* Literature review assistance
* Research paper understanding
* Thesis preparation
* Research gap identification
* Academic project planning
* Scientific paper evaluation
* Medical paper safety review

---

## 🎯 Kaggle AI Agents Capstone Concepts Demonstrated

This project demonstrates multiple concepts from the Google × Kaggle AI Agents Intensive:

✅ Multi-Agent Systems

✅ Agent Skills

✅ Security & Safety Evaluation

✅ Human-in-the-Loop Review

✅ Vibe Coding Workflow

---

## 🔮 Future Improvements

* MCP Server Integration
* ADK Agent Orchestration
* Citation Verification Agent
* ArXiv/PubMed Search Agent
* Research Gap Detection Agent
* Paper-to-Presentation Generator
* Automatic Literature Review Builder
* Multi-PDF Comparative Analysis

---

## 👩‍💻 Author

**Rinvi Jaman Riti**

B.Sc. in Computer Science & Engineering
Daffodil International University

GitHub: https://github.com/rinviriti

---

## 📜 License

This project is released under the MIT License.
