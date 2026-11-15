# Lab 5 – Reflection

**Student:** YASHAS V  
**SRN:** PES2UG24AM188

### 1. What is static code analysis and why is it useful?

Static code analysis examines source code without executing the program. It helps identify likely bugs, insecure coding patterns and style problems early. This makes code easier to maintain and reduces the chance of defects reaching users.

### 2. What is the difference between Pylint, Bandit and Flake8?

Pylint checks code quality, possible logical errors, naming, unused variables and design issues. Bandit focuses on common Python security weaknesses. Flake8 checks style and formatting rules, including PEP 8 conventions.

### 3. Which issues were identified and how were they fixed?

The original program stored a bank-sync password in the source, used `tempfile.mktemp()`, constructed a shell command with `os.system()`, caught every exception in `biggestExpense()`, and lacked input validation and consistent naming. The password is now read from an environment variable, temporary files are securely created, statement opening uses `webbrowser`, the empty-ledger case is handled explicitly, and the code uses validation, type hints and snake_case names.

### 4. How does static analysis improve software quality?

It provides repeatable feedback before runtime, helps developers prioritize security and reliability problems, encourages consistent style, and makes code reviews more effective. It does not replace tests or human review, but it complements them.
