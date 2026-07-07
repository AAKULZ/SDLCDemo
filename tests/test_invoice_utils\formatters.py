import pytest
import invoice_utils.formatters

def test_format_currency_usd():
    assert invoice_utils.formatters.format_currency(19.9) == "$19.90"

def test_format_currency_eur():
    assert invoice_utils.formatters.format_currency(100.55, currency="EUR") == "â‚¬100.55"

def test_format_currency_gbp():
    assert invoice_utils.formatters.format_currency(50.0, currency="GBP") == "Â£50.00"

def test_format_currency_inr():
    assert invoice_utils.formatters.format_currency(1234.56, currency="INR") == "â‚¹1,234.56"

def test_format_currency_unknown():
    assert invoice_utils.formatters.format_currency(75.25, currency="CAD") == "CAD 75.25"

def test_format_currency_zero():
    assert invoice_utils.formatters.format_currency(0) == "$0.00"

def test_format_currency_negative():
    assert invoice_utils.formatters.format_currency(-10.50) == "$-10.50"

def test_format_invoice_number_normal():
    assert invoice_utils.formatters.format_invoice_number(42) == "INV-000042"

def test_format_invoice_number_zero():
    assert invoice_utils.formatters.format_invoice_number(0) == "INV-000000"

def test_format_invoice_number_large():
    assert invoice_utils.formatters.format_invoice_number(1234567) == "INV-1234567"

def test_format_invoice_number_custom_prefix():
    assert invoice_utils.formatters.format_invoice_number(99, prefix="PO") == "PO-000099"

def test_format_invoice_number_negative_raises_error():
    with pytest.raises(ValueError, match="invoice number cannot be negative"):
        invoice_utils.formatters.format_invoice_number(-1)

def test_format_percentage_normal():
    assert invoice_utils.formatters.format_percentage(0.075) == "7.5%"

def test_format_percentage_zero():
    assert invoice_utils.formatters.format_percentage(0) == "0.0%"

def test_format_percentage_one():
    assert invoice_utils.formatters.format_percentage(1) == "100.0%"

def test_format_percentage_decimal():
    assert invoice_utils.formatters.format_percentage(0.12345) == "12.3%"

def test_truncate_description_short():
    assert invoice_utils.formatters.truncate_description("Short description") == "Short description"

def test_truncate_description_exact_length():
    description = "A" * 40
    assert invoice_utils.formatters.truncate_description(description) == description

def test_truncate_description_longer():
    long_description = "This is a very long description that needs to be truncated."
    expected_truncation = "This is a very long description that needs to be â€¦"
    assert invoice_utils.formatters.truncate_description(long_description) == expected_truncation

def test_truncate_description_max_length_one():
    assert invoice_utils.formatters.truncate_description("abcdef", max_length=1) == "â€¦"

def test_truncate_description_max_length_zero():
    assert invoice_utils.formatters.truncate_description("abcdef", max_length=0) == "â€¦"

def test_truncate_description_trailing_space():
    description = "This description has a trailing space.   "
    expected_truncation = "This description has a trailing spaâ€¦"
    assert invoice_utils.formatters.truncate_description(description, max_length=40) == expected_truncation
