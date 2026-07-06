"""
calculations.py
Core numeric calculations for invoice line items: tax, discounts,
currency conversion, and line totals. These are pure functions with
full test coverage (see tests/test_calculations.py) — a good example
of a "healthy" module in the Build & Test report.
"""


def calculate_tax(amount, rate):
    """Returns the tax amount for a given base amount and tax rate (0-1)."""
    if rate < 0:
        raise ValueError("tax rate cannot be negative")
    return round(amount * rate, 2)


def apply_discount(amount, percent):
    """Applies a percentage discount (0-100) to an amount."""
    if not (0 <= percent <= 100):
        raise ValueError("discount percent must be between 0 and 100")
    return round(amount * (1 - percent / 100), 2)


def convert_currency(amount, rate):
    """Converts an amount using a positive exchange rate."""
    if rate <= 0:
        raise ValueError("exchange rate must be positive")
    return round(amount * rate, 2)


def calculate_line_total(quantity, unit_price, tax_rate=0.0):
    """Computes the total for a line item: quantity * unit_price, plus tax."""
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    subtotal = quantity * unit_price
    tax = calculate_tax(subtotal, tax_rate)
    return round(subtotal + tax, 2)
