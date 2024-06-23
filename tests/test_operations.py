import pytest
from decimal import Decimal
from operations import do_deposit


def test_deposit(user):
    assert user.balance == Decimal("0,0")
