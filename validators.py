"""
validators.py
Input validation helpers for invoice fields. The source code here is
correct; one test in tests/test_validators.py has an intentionally wrong
expectation, to demonstrate the "test bug vs source bug" distinction the
AI Analysis step is meant to make clear during the demo.
"""

import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_INVOICE_RE = re.compile(r"^INV-\d{6}$")
_CURRENCY_RE = re.compile(r"^[A-Z]{3}$")


def is_valid_email(email):
    """Very small pragmatic email check (not RFC 5322-complete)."""
    if not email or not isinstance(email, str):
        return False
    return bool(_EMAIL_RE.match(email))


def is_valid_invoice_number(invoice_no):
    """Invoice numbers must look like INV-000123 (INV- plus exactly 6 digits)."""
    if not invoice_no or not isinstance(invoice_no, str):
        return False
    return bool(_INVOICE_RE.match(invoice_no))


def is_valid_amount(amount):
    """Amounts must be a positive number."""
    if isinstance(amount, bool):
        return False
    if not isinstance(amount, (int, float)):
        return False
    return amount > 0


def is_valid_currency_code(code):
    """Currency codes must be exactly 3 uppercase letters (e.g. USD, EUR)."""
    if not code or not isinstance(code, str):
        return False
    return bool(_CURRENCY_RE.match(code))
