"""domain models for bill_audit"""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class EnergyConsumption:
    #Energy consumption reported in a bill.
    total_kwh: Decimal
    measured_kwh: Decimal | None=None   #this means that the field can have a Decimal value or None which means value not available
    estimated_kwh: Decimal | None=None  #this is different than saying estimated_kwh=Decimal("0") because that would mean that the bill shows 0 kwh measured, 
                                        #instead we're saying that the data is not available

    def __post_init__(self)->None:
        #validate consumption values.
        if self.total_kwh<Decimal("0"):
            raise ValueError("Total consumption cannot be negative")
        if (self.measured_kwh is not None and self.measured_kwh<Decimal("0")):
            raise ValueError("Measured consumption cannot be negative.")
        if (self.estimated_kwh is not None and self.estimated_kwh<Decimal("0")):
            raise ValueError("estimated consumption cannot be negative.")


@dataclass(frozen=True)
class Bill:
    #essential information extracted from an energy bill
    provider:str
    bill_number:str
    issue_date:date
    billing_period_start:date
    billing_period_end:date
    total_amount:Decimal
    currency:str="EUR"
    consumption: EnergyConsumption | None=None

    def __post_init__(self) -> None:
        """Validate the bill after its creation."""
        if not self.provider.strip():
            raise ValueError("Provider cannot be empty.")

        if not self.bill_number.strip():
            raise ValueError("Bill number cannot be empty.")

        if self.billing_period_end < self.billing_period_start:
            raise ValueError(
                "Billing period end cannot be before its start."
            )

        if self.total_amount < Decimal("0"):
            raise ValueError("Total amount cannot be negative.")
        
"""
normally you would have had to manually write the __init__ method to initialize the attributes of the class, 
but with @dataclass, this is done automatically. The __post_init__ method is a special method that is called 
after the __init__ method, and it is used here to validate the attributes of the Bill class. If any of the validation
checks fail, a ValueError is raised with an appropriate message.

frozen=True means that once created, the attributes of the bill are immutable

total_amount:Decimal means that the total_amount attribute is of type Decimal, which is a more precise way to represent 
decimal numbers than using float. This is important because python does not impose the type so you have to check it yourself.

we cannot use float because for example the addition of 0.1 and 0.2 in float does not give exactly 0.3 due to the way floating
point numbers are represented in binary. meanwhile Decimal can represent number exactly as they are written

why are there 2 separate classes? we could just add
total_kwh: Decimal
measured_kwh: Decimal
estimated_kwh: Decimal
in Bill, but Bill would get progressivly big, with composition every obj has its own scope. and it is more readble than a big 
class with many indipendent fields.
"""

