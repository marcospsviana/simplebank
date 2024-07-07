from decimal import Context, Decimal

import pytest
from sqlmodel import Session, select

from database_operations import BaseOps
from models import Account, User
from operations import do_deposit


def test_deposit(session, user, account):
    do_deposit(1200, account=account.account_number)
    session.flush(account)
    base_ops = BaseOps()
    account_user = base_ops.get_account(user.id)
    assert account_user.balance == 1200.0

