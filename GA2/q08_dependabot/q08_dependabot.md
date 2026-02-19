# GA2 — Q8: Configure Dependabot for Security Updates

## Problem Summary

Configure Dependabot for a Python project such that:

- A `requirements.txt` file exists with at least 3 dependencies.
- A `.github/dependabot.yml` file exists with the correct structure.
- `README.md` contains my IITM email.
- The repository is public.

---

## Repository Used

**Repository Name:**  
TDS-Jan-2026  

**Repository URL:**  
https://github.com/AshkaPathak/TDS-Jan-2026  

The repository is public.

---

## Project Structure

The required files were created at the repository root:

```
TDS-Jan-2026/
│
├── requirements.txt
├── README.md
└── .github/
    └── dependabot.yml
```

---

## requirements.txt

Contains at least three Python dependencies:

```
fastapi
requests
pandas
```

This satisfies the minimum dependency requirement.

---

## Dependabot Configuration

**Path:**

```
.github/dependabot.yml
```

**Contents:**

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    commit-message:
      prefix: "deps"
```

This configuration ensures:

- Package ecosystem: `pip`
- Monitoring the root directory (`/`)
- Weekly dependency checks
- Commit messages prefixed with `deps`

---

## README Update

The `README.md` contains the required IITM email:

```
23f3002663@ds.study.iitm.ac.in
```

---

## GitHub Commands Used

```bash
cd ~/TDS-Jan-2026

nano requirements.txt
mkdir -p .github
nano .github/dependabot.yml
nano README.md

git add requirements.txt .github/dependabot.yml README.md
git commit -m "GA2 Q8: configure Dependabot for Python project"
git push
```

---

## Verification

The grader verifies:

✔ `.github/dependabot.yml` exists with correct structure  
✔ `requirements.txt` has at least 3 dependencies  
✔ `README.md` contains IITM email  
✔ Repository is public  

---

## Conclusion

Dependabot was successfully configured for the Python project with correct structure, dependencies, and email inclusion in the README.

