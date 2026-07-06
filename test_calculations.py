import pytest
from invoice_utils.calculations import (
    calculate_tax,
    apply_discount,
    convert_currency,
    calculate_line_total,
)


def test_calculate_tax_basic():
    assert calculate_tax(100, 0.2) == 20.0


def test_calculate_tax_zero_rate():
    assert calculate_tax(100, 0) == 0.0


def test_calculate_tax_negative_rate_raises():
    with pytest.raises(ValueError):
        calculate_tax(100, -0.1)


def test_apply_discount_basic():
    assert apply_discount(200, 25) == 150.0


def test_apply_discount_zero_percent():
    assert apply_discount(200, 0) == 200.0


def test_apply_discount_out_of_range_raises():
    with pytest.raises(ValueError):
        apply_discount(200, 150)


def test_convert_currency_basic():
    assert convert_currency(100, 1.1) == 110.0


def test_convert_currency_invalid_rate_raises():
    with pytest.raises(ValueError):
        convert_currency(100, 0)


def test_calculate_line_total_no_tax():
    assert calculate_line_total(3, 10.0) == 30.0


def test_calculate_line_total_with_tax():
    assert calculate_line_total(2, 50.0, tax_rate=0.1) == 110.0


def test_calculate_line_total_negative_quantity_raises():
    with pytest.raises(ValueError):
        calculate_line_total(-1, 10.0)
