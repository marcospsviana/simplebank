from datetime import datetime, timezone

from sqlmodel import select

from database_operations import BaseOps, OperationsAccount
from models import LimitWithDrawal
from operations import do_deposit, do_withdrawal


def test_deposit(session, user, account):
    print(f"ACCOUNT NUMBER {account.account_number}")
    do_deposit(1200, account=f"{account.account_number}")
    base_ops = BaseOps()
    account_user = base_ops.get_account(user.id)
    assert account_user.balance == 1200.0


def test_withdrawal(user, account):
    do_withdrawal(600, account=f"{account.account_number}")
    base_ops = BaseOps()
    account_user = base_ops.get_account(user.id)
    assert account_user.balance == 600.0


def test_withdrawal_over_balance(account):
    result = do_withdrawal(6000, account=f"{account.account_number}")
    assert (
        result
        == "Account doesn't have enough to withdrawal $ 6000.0, account balance: $ 600.0"
    )


def test_unique_account_per_user(account):
    base_ops = BaseOps()
    result = base_ops.create_new_register_account(account_user="test-name")
    assert (
        result
        == f"Account for this costumer already exists, account number: {account.account_number}"
    )


def test_record_extract(account):
    operation = OperationsAccount()
    result = operation.get_extract(f"{account.account_number}")
    assert len(result) == 2


def test_limit_withdrawal(account):
    do_withdrawal(60, account=f"{account.account_number}")
    do_withdrawal(60, account=f"{account.account_number}")
    do_withdrawal(60, account=f"{account.account_number}")
    result = do_withdrawal(60, account=f"{account.account_number}")
    assert (
        result
        == "You already have made three withdrawals today this is the limit daily!"
    )


def test_deposit_wrong_value(account):
    result = do_deposit(-60, account=f"{account.account_number}")
    assert result == "This value $ -60 is not allowed!"


def test_withdraw_update_date(session, account):
    current_date = datetime.now(timezone.utc)
    limit_statement = select(LimitWithDrawal).where(
        LimitWithDrawal.account == account.id
    )
    limit = session.exec(limit_statement)
    limit_withdrawal = limit.first()
    date_withdrawal = datetime.fromisoformat(f"{limit_withdrawal.date_withdrawal}")
    assert date_withdrawal.date() == current_date.date()
