from datetime import date
from decimal import Decimal

import pytest

from bill_audit.models import Bill


def test_create_valid_bill():
    bill = Bill(
        provider="Example Energy",
        bill_number="INV-001",
        issue_date=date(2026, 9, 1),
        billing_period_start=date(2026, 7, 1),
        billing_period_end=date(2026, 8, 31),
        total_amount=Decimal("84.37"),
    )

    assert bill.provider == "Example Energy"
    assert bill.total_amount == Decimal("84.37")
    assert bill.currency == "EUR"


def test_reject_empty_provider():
    with pytest.raises(ValueError, match="Provider cannot be empty"):
        Bill(
            provider="   ",
            bill_number="INV-001",
            issue_date=date(2026, 9, 1),
            billing_period_start=date(2026, 7, 1),
            billing_period_end=date(2026, 8, 31),
            total_amount=Decimal("84.37"),
        )


def test_reject_invalid_billing_period():
    with pytest.raises(
        ValueError,
        match="Billing period end cannot be before its start",
    ):
        Bill(
            provider="Example Energy",
            bill_number="INV-001",
            issue_date=date(2026, 9, 1),
            billing_period_start=date(2026, 8, 31),
            billing_period_end=date(2026, 7, 1),
            total_amount=Decimal("84.37"),
        )


def test_reject_negative_total():
    with pytest.raises(ValueError, match="Total amount cannot be negative"):
        Bill(
            provider="Example Energy",
            bill_number="INV-001",
            issue_date=date(2026, 9, 1),
            billing_period_start=date(2026, 7, 1),
            billing_period_end=date(2026, 8, 31),
            total_amount=Decimal("-1.00"),
        )


"""
this file contains unit tests for the Bill class in the bill_audit.models module. The tests use the pytest framework
to verify that the Bill class behaves as expected when creating valid bills and when rejecting invalid bills. Each test
function checks a specific aspect of the Bill class, such as creating a valid bill, rejecting an empty provider, rejecting
an invalid billing period, and rejecting a negative total amount. The tests use assertions to check that the expected
exceptions are raised and that the attributes of the Bill instance are set correctly.
"""