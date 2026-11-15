# Lab 5 – Static Code Analysis Issue Table

**Student:** YASHAS V  
**SRN:** PES2UG24AM188  
**Section:** 5C  
**Application:** Personal Expense Tracker

| Issue | Type | Original location | Description / risk | Fix approach |
|---|---|---:|---|---|
| Hardcoded bank-sync password | Security (high) | Original line 5 | Secret embedded in source can be exposed through repository history. | Read the secret from `BANK_SYNC_PASSWORD` environment variable. |
| Unsafe temporary filename | Security (high) | Original `exportReport`, line 36 | `tempfile.mktemp()` creates a race condition because the file is not securely created. | Use `NamedTemporaryFile(delete=False)` to create the file atomically. |
| Shell command construction | Security (high) | Original `openStatement`, line 42 | `os.system("xdg-open " + path)` passes user-controlled text through a shell and is platform-specific. | Use `webbrowser.open()` with a resolved file URI; verify the file exists. |
| Broad exception handling | Reliability | Original `biggestExpense`, lines 29–32 | `except Exception` hides unrelated programming errors. | Check for an empty ledger explicitly, then call `max()`. |
| Password comparison | Security | Original `checkSyncPassword`, line 33 | Ordinary equality comparison is not designed for secret comparison. | Use `hmac.compare_digest()` and fail closed if no secret is configured. |
| Naming and formatting violations | Style / maintainability | Throughout original file | Mixed camelCase names, spacing, long lines and missing docstrings reduce readability and tool compliance. | Use snake_case, type hints, docstrings and consistent formatting. |
| Unvalidated budget | Reliability | Original `setBudget`, line 24 | Negative or non-numeric budgets can produce invalid application state. | Validate the value before updating the global budget. |
| Import-time execution | Maintainability | Original final line | Importing the module immediately runs the demonstration. | Protect execution with `if __name__ == "__main__":`. |

## Verification

The corrected program is `expense_tracker.py`. Run the three static-analysis tools locally using the commands in `README.md`. Tool output is intentionally not fabricated: the execution environment used to prepare this package did not have Pylint, Bandit or Flake8 installed.
