"""domain models for bill_audit"""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

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
"""