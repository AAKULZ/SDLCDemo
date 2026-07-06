from invoice_utils.validators import (
    is_valid_email,
    is_valid_invoice_number,
    is_valid_amount,
    is_valid_currency_code,
)


def test_valid_email_accepts_normal_address():
    assert is_valid_email("finance@client.com") is True


def test_valid_email_rejects_missing_at():
    assert is_valid_email("financeclient.com") is False


def test_valid_email_rejects_empty():
    assert is_valid_email("") is False


def test_invoice_number_accepts_full_format():
    assert is_valid_invoice_number("INV-000123") is True


def test_invoice_number_rejects_short_form():
    # NOTE: this is the demo repo's intentional "test bug" — whoever wrote
    # this test assumed short invoice numbers like "INV-123" were valid,
    # but the validator (correctly, per the module's own docstring)
    # requires exactly 6 digits. The source code is right; this
    # assertion's expectation is wrong. Good example for the AI Analysis
    # step to point out "this looks like a test bug, not a source bug."
    assert is_valid_invoice_number("INV-123") is True


def test_invoice_number_rejects_missing_prefix():
    assert is_valid_invoice_number("000123") is False


def test_valid_amount_accepts_positive():
    assert is_valid_amount(49.99) is True


def test_valid_amount_rejects_zero():
    assert is_valid_amount(0) is False


def test_valid_amount_rejects_negative():
    assert is_valid_amount(-5) is False


def test_valid_currency_code_accepts_usd():
    assert is_valid_currency_code("USD") is True


def test_valid_currency_code_rejects_lowercase():
    assert is_valid_currency_code("usd") is False
