"""
formatters.py
Display-formatting helpers for invoices. Deliberately has NO test file in
this repo — it's the intended target for the Build Agent's "Generate
Tests" step during the demo, since the Build & Test report will show it
as a coverage gap.
"""


def format_currency(amount, currency="USD"):
    """Formats a number as a currency string, e.g. format_currency(19.9) -> '$19.90'."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "INR": "₹"}
    symbol = symbols.get(currency, currency + " ")
    return f"{symbol}{amount:,.2f}"


def format_invoice_number(number, prefix="INV"):
    """Formats an integer invoice number with zero-padding, e.g. 42 -> 'INV-000042'."""
    if number < 0:
        raise ValueError("invoice number cannot be negative")
    return f"{prefix}-{number:06d}"


def format_percentage(value):
    """Formats a 0-1 ratio as a percentage string, e.g. 0.075 -> '7.5%'."""
    return f"{value * 100:.1f}%"


def truncate_description(description, max_length=40):
    """Truncates a line-item description to max_length, adding an ellipsis."""
    if len(description) <= max_length:
        return description
    return description[: max_length - 1].rstrip() + "…"
