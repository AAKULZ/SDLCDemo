import pytest
import invoice_utils.formatters

def test_format_currency_usd():
    assert invoice_utils.formatters.format_currency(19.9) == "$19.90"

def test_format_currency_eur():
    assert invoice_utils.formatters.format_currency(1234.567, currency="EUR") == "â‚¬1,234.57"

def test_format_currency_gbp():
    assert invoice_utils.formatters.format_currency(0.5, currency="GBP") == "Â£0.50"

def test_format_currency_inr():
    assert invoice_utils.formatters.format_currency(1000000, currency="INR") == "â‚¹1,000,000.00"

def test_format_currency_unknown():
    assert invoice_utils.formatters.format_currency(50, currency="CAD") == "CAD 50.00"

def test_format_currency_zero():
    assert invoice_utils.formatters.format_currency(0) == "$0.00"

def test_format_invoice_number_normal():
    assert invoice_utils.formatters.format_invoice_number(42) == "INV-000042"

def test_format_invoice_number_custom_prefix():
    assert invoice_utils.formatters.format_invoice_number(100, prefix="PO") == "PO-000100"

def test_format_invoice_number_zero():
    assert invoice_utils.formatters.format_invoice_number(0) == "INV-000000"

def test_format_invoice_number_large():
    assert invoice_utils.formatters.format_invoice_number(999999) == "INV-999999"

def test_format_invoice_number_negative_raises_error():
    with pytest.raises(ValueError, match="invoice number cannot be negative"):
        invoice_utils.formatters.format_invoice_number(-10)

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
    long_desc = "This is a very long description that needs to be truncated."
    expected = "This is a very long description that needs to be trunâ€¦"
    assert invoice_utils.formatters.truncate_description(long_desc) == expected

def test_truncate_description_max_length_one():
    assert invoice_utils.formatters.truncate_description("abcdef", max_length=1) == "â€¦"

def test_truncate_description_max_length_zero():
    assert invoice_utils.formatters.truncate_description("abcdef", max_length=0) == "â€¦"

def test_truncate_description_with_trailing_space():
    long_desc = "This description has a trailing space. "
    expected = "This description has a trailing space.â€¦"
    assert invoice_utils.formatters.truncate_description(long_desc, max_length=40) == expected

def test_module_loads():
    # This test ensures the module can be imported without errors.
    # The functions in this module are pure and have straightforward logic,
    # making them amenable to direct testing as done above.
    assert True