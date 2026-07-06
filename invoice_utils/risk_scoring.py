"""
risk_scoring.py
Aggregates per-invoice risk scores for a batch (e.g. fraud/late-payment
risk). NOTE: `average_risk_score` has a genuine bug — it doesn't guard
against an empty batch, so it raises a raw ZeroDivisionError instead of a
clear, documented error. This is intentional: it's the "real" bug this
demo repo ships with, meant to be caught by the Build & Test step and
explained by the AI Analysis step.
"""


def classify_risk(score):
    """Buckets a 0-100 risk score into a label."""
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score < 30:
        return "low"
    if score < 70:
        return "medium"
    return "high"


def average_risk_score(scores):
    """Returns the mean of a list of per-invoice risk scores.

    BUG: does not handle an empty `scores` list, so calling this with []
    raises ZeroDivisionError instead of a clear, documented error. Left
    in deliberately for the demo -- ask the Build Agent's AI Analysis
    step to explain the failing test that exercises this.
    """
    total = sum(scores)
    return round(total / len(scores), 2)


def flagged_ratio(flagged_count, total_count):
    """Returns what fraction of a batch was flagged as high-risk."""
    if flagged_count < 0 or total_count < 0:
        raise ValueError("counts cannot be negative")
    if flagged_count > total_count:
        raise ValueError("flagged_count cannot exceed total_count")
    if total_count == 0:
        return 0.0
    return round(flagged_count / total_count, 4)
