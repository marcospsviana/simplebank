from database_operations import BaseOps
from operations import do_deposit, do_withdrawal


def test_deposit(session, user, account):
    do_deposit(1200, account=account.account_number)
    base_ops = BaseOps()
    account_user = base_ops.get_account(user.id)
    assert account_user.balance == 1200.0


def test_withdrawal(session, user, account):
    do_withdrawal(600, account=account.account_number)
    base_ops = BaseOps()
    account_user = base_ops.get_account(user.id)
    assert account_user.balance == 600.0


def test_unique_account_per_user(session, user, account):
    base_ops = BaseOps()
    result = base_ops.create_new_register_account(account_user=user.name)
    assert (
        result
        == f"Account for this costumer already exists, account number; {account.account_number}"
    )
