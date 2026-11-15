"""Personal expense tracker with safe report and bank-sync helpers."""

from __future__ import annotations

import hmac
import os
import tempfile
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Any

DEFAULT_BUDGET = 20_000
REPORT_DIR = Path(tempfile.gettempdir()) / "expense_reports"
BANK_SYNC_PASSWORD_ENV = "BANK_SYNC_PASSWORD"

expenses: list[dict[str, Any]] = []
monthly_budget = DEFAULT_BUDGET


def add_expense(amount: float, category: str = "Misc", note: str = "") -> bool:
    """Record a positive expense; reject invalid amounts."""
    if (
        not isinstance(amount, (int, float))
        or isinstance(amount, bool)
        or amount <= 0
    ):
        print("Ignoring invalid amount", amount)
        return False
    expenses.append(
        {
            "amount": amount,
            "category": category,
            "note": note,
            "time": datetime.now().isoformat(),
        }
    )
    return True


def total_by_category() -> dict[str, float]:
    """Return spending totals grouped by category."""
    totals: dict[str, float] = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return totals


def set_budget(new_budget: float) -> bool:
    """Set a non-negative monthly budget."""
    global monthly_budget
    if (
        not isinstance(new_budget, (int, float))
        or isinstance(new_budget, bool)
    ):
        return False
    if new_budget < 0:
        return False
    monthly_budget = new_budget
    return True


def remaining_budget() -> float:
    """Return the budget remaining after recorded expenses."""
    spent = sum(expense["amount"] for expense in expenses)
    return monthly_budget - spent


def biggest_expense() -> dict[str, Any] | None:
    """Return the largest expense, or None when the ledger is empty."""
    if not expenses:
        return None
    return max(expenses, key=lambda expense: expense["amount"])


def print_ledger() -> None:
    """Print all recorded expenses in insertion order."""
    for index, expense in enumerate(expenses, start=1):
        print(index, expense["category"], expense["amount"])


def check_sync_password(password: str) -> bool:
    """Compare a supplied password with the environment-configured secret."""
    expected = os.environ.get(BANK_SYNC_PASSWORD_ENV)
    if not expected or not isinstance(password, str):
        return False
    return hmac.compare_digest(password, expected)


def export_report() -> str:
    """Create an empty report file securely and return its path."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".txt", dir=REPORT_DIR, delete=False
    ) as report_file:
        return report_file.name


def open_statement(path: str) -> bool:
    """Open an existing statement using the platform's registered handler."""
    statement = Path(path).expanduser().resolve()
    if not statement.is_file():
        return False
    return bool(webbrowser.open(statement.as_uri()))


def main() -> None:
    """Run a short demonstration of the expense tracker."""
    print("Biggest expense before any entries:", biggest_expense())
    add_expense(450, "Food", "Lunch with team")
    add_expense(1200, "Travel", "Cab to airport")
    add_expense(-50, "Food")
    add_expense(300, "Food", "Groceries")
    add_expense(999, "Bills", "Internet")
    set_budget(5000)
    print_ledger()
    print("Totals:", total_by_category())
    print("Remaining budget:", remaining_budget())
    largest = biggest_expense()
    print("Biggest expense:", largest["note"] if largest else None)
    print("Sync password accepted:", check_sync_password("guess"))
    print(
        "Summary:",
        len(expenses),
        "expenses recorded against a budget of",
        monthly_budget,
    )


if __name__ == "__main__":
    main()
