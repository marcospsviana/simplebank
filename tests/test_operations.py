from decimal import Context, Decimal

import pytest
from sqlmodel import Session, select

from database_operations import BaseOps
from models import Account, User
from operations import do_deposit

base_ops = BaseOps()


def test_deposit(session, user, account):
    do_deposit(1200, account=account.account_number)
    session.flush(account)
    account_user = base_ops.get_account(user.id)
    assert account_user.balance == 1200.0

def test_unique_account_per_user(session, user, account):
    result = base_ops.create_new_register_account(account_user=user.name)
    assert result == f"Account for this costumer already exists, account number; {account.account_number}"