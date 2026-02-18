# TDS Jan 2026 — Assignment Attempts

This repository documents **how I attempt and solve questions** from the **Tools in Data Science (TDS)** course.

It is structured to reflect my thinking process, debugging strategy, and deployment workflow — not just final answers.

---

## Philosophy

This repository is not just a submission archive.

Each question is approached with:

- Clear problem breakdown  
- Identification of constraints and edge cases  
- Structured solution strategy  
- Reproducible commands and code  
- Deployment and verification steps  
- Clean Git history that reflects iteration and debugging  

The focus is on clarity, reproducibility, and technical discipline.

---

## Repository Structure

```
TDS-Jan-2026/
│
├── GA1/                  # Graded Assignment 1
│   ├── q01_*.md          # Question-wise writeups
│   ├── dataflow-pipeline/
│   ├── email.json
│   └── ...
│
├── GA2/                  # Graded Assignment 2
│   ├── q01_*.md
│   ├── q02_*.md
│   └── ...
│
└── README.md
```

Each GA folder is self-contained and contains all related artifacts for that assignment.

---

## Question Documentation Format

Each question markdown file typically contains:

### 1. Problem Summary  
Clear restatement of the problem.

### 2. Constraints / Common Failure Points  
Validation errors, formatting requirements, and edge cases.

### 3. Strategy  
Reasoned approach before implementation.

### 4. Implementation  
Commands, scripts, configuration, or code used to solve the problem.

### 5. Verification  
How the output was validated (CLI checks, API tests, hashes, etc.).

### 6. GitHub Steps  
Exact steps used to structure and push the solution.

---

## Tools Used

- Python 3.11+
- FastAPI
- uv / pip
- Git & GitHub
- Bash utilities
- JSON and Markdown
- Deployment platforms (e.g., Render when required)

---

## Workflow Discipline

- `git mv` used to preserve history when restructuring  
- Question-wise commits with descriptive messages  
- Clean folder separation between assignments  
- Deterministic outputs wherever possible  
- No unnecessary large files  

---

## Purpose of This Repository

This repository serves as:

- A structured record of my TDS learning process  
- A reproducible reference for deployment-heavy questions  
- A technical audit trail of my problem-solving approach  

It reflects both correctness and method.

---

## Author

Ashka Pathak  