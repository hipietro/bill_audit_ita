from datetime import date
from decimal import Decimal

import pytest

from bill_audit.models import (
    Bill,
    CostCategory,
    CostComponent,
    EnergyConsumption,
)


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

def test_create_energy_consumption():
    consumption=EnergyConsumption(
        total_kwh=Decimal("241.50"),
        measured_kwh=Decimal("200.00"),
        estimated_kwh=Decimal("41.50"),
    )

    assert consumption.total_kwh==Decimal("241.50")
    assert consumption.measured_kwh == Decimal("200.00")
    assert consumption.estimated_kwh == Decimal("41.50")

def test_bill_can_contain_consumption():
    consumption = EnergyConsumption(
        total_kwh=Decimal("241.50"),
        measured_kwh=Decimal("200.00"),
        estimated_kwh=Decimal("41.50"),
    )

    bill = Bill(
        provider="Example Energy",
        bill_number="INV-001",
        issue_date=date(2026, 9, 1),
        billing_period_start=date(2026, 7, 1),
        billing_period_end=date(2026, 8, 31),
        total_amount=Decimal("84.37"),
        consumption=consumption,
    )

    assert bill.consumption is consumption #here we use is because == checks if 2 obj have the same value but is checks if they're the same obj in memory
                                           #and since we want to verify that Bill stores EnergyConsumption that we provided
    assert bill.consumption.total_kwh == Decimal("241.50")


def test_reject_negative_total_consumption():
    with pytest.raises(
        ValueError,
        match="Total consumption cannot be negative",
    ):
        EnergyConsumption(
            total_kwh=Decimal("-1.00"),
        )

def test_create_cost_component():
    component = CostComponent(
        category=CostCategory.ENERGY_SALES,
        description="Vendita energia",
        amount=Decimal("50.00"),
    )

    assert component.category == CostCategory.ENERGY_SALES
    assert component.description == "Vendita energia"
    assert component.amount == Decimal("50.00")


def test_reject_empty_cost_component_description():
    with pytest.raises(
        ValueError,
        match="Cost component description cannot be empty",
    ):
        CostComponent(
            category=CostCategory.OTHER_ITEM,
            description="   ",
            amount=Decimal("5.00"),
        )


def test_allow_negative_discount():
    discount = CostComponent(
        category=CostCategory.DISCOUNT,
        description="Sconto commerciale",
        amount=Decimal("-5.00"),
    )

    assert discount.amount == Decimal("-5.00")


def test_bill_calculates_cost_components_total():
    energy = CostComponent(
        category=CostCategory.ENERGY_SALES,
        description="Vendita energia",
        amount=Decimal("50.00"),
    )
    network = CostComponent(
        category=CostCategory.NETWORK_AND_SYSTEM_CHARGES,
        description="Rete e oneri",
        amount=Decimal("10.00"),
    )
    vat = CostComponent(
        category=CostCategory.VAT,
        description="IVA",
        amount=Decimal("6.60"),
    )
    discount = CostComponent(
        category=CostCategory.DISCOUNT,
        description="Sconto commerciale",
        amount=Decimal("-5.00"),
    )

    bill = Bill(
        provider="Example Energy",
        bill_number="INV-001",
        issue_date=date(2026, 9, 1),
        billing_period_start=date(2026, 7, 1),
        billing_period_end=date(2026, 8, 31),
        total_amount=Decimal("61.60"),
        cost_components=(
            energy,
            network,
            vat,
            discount,
        ),
    )

    assert bill.components_total == Decimal("61.60")


"""

"""