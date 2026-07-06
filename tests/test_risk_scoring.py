import pytest
from invoice_utils.risk_scoring import (
    classify_risk,
    average_risk_score,
    flagged_ratio,
)


def test_classify_risk_low():
    assert classify_risk(10) == "low"


def test_classify_risk_medium():
    assert classify_risk(50) == "medium"


def test_classify_risk_high():
    assert classify_risk(90) == "high"


def test_classify_risk_out_of_range_raises():
    with pytest.raises(ValueError):
        classify_risk(150)


def test_average_risk_score_basic():
    assert average_risk_score([10, 20, 30]) == 20.0


def test_average_risk_score_single_value():
    assert average_risk_score([42]) == 42.0


def test_average_risk_score_empty_batch_should_not_crash():
    # This is the demo repo's intentional REAL bug: an empty batch (e.g. a
    # day with zero invoices processed) should be a normal, expected case,
    # not a crash. `average_risk_score` currently divides by len(scores)
    # with no guard, so this raises ZeroDivisionError instead of behaving
    # sensibly. This test is written the way a reasonable engineer would
    # write it against the intended behavior -- it's expected to FAIL
    # against the current buggy implementation, which is the point: run
    # it through the Build Agent's Build & Test step, then use "Ask AI to
    # explain this" on the failure.
    assert average_risk_score([]) == 0.0


def test_flagged_ratio_basic():
    assert flagged_ratio(3, 12) == 0.25


def test_flagged_ratio_zero_total():
    assert flagged_ratio(0, 0) == 0.0


def test_flagged_ratio_flagged_exceeds_total_raises():
    with pytest.raises(ValueError):
        flagged_ratio(5, 2)
