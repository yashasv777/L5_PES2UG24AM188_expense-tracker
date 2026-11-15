# Lab 5 – Static Code Analysis

Student: **YASHAS V** | SRN: **PES2UG24AM188** | Section: **5C**

## Setup and run

```bash
python -m venv venv
# Windows PowerShell:
venv\Scripts\Activate.ps1
# macOS/Linux:
# source venv/bin/activate

python -m pip install pylint bandit flake8
python expense_tracker.py
```

## Capture baseline reports

Run these commands against the original starter file before replacing it, if your instructor requires the raw before reports:

```bash
python -m pylint expense_tracker.py > pylint_before.txt
python -m bandit -r expense_tracker.py > bandit_before.txt
python -m flake8 expense_tracker.py > flake8_before.txt
```

## Final reports

```bash
python -m pylint expense_tracker.py > pylint_after.txt
python -m bandit -r expense_tracker.py > bandit_after.txt
python -m flake8 expense_tracker.py > flake8_after.txt
```

Review the reports and retain terminal screenshots. The package does not claim a score or a clean scan until these commands have actually been run with the tools installed.

## Commit

```bash
git add expense_tracker.py issues.md reflection.md
git commit -m "Fix static analysis issues in expense tracker"
```

A second and third commit can separate the security and style fixes if your instructor expects three commits, but do not create empty or misleading commits.
