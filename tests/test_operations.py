from database_operations import BaseOps, OperationsAccount
from operations import do_deposit, do_withdrawal


def test_deposit(session, user, account):
    do_deposit(1200, account=account.account_number)
    base_ops = BaseOps()
    account_user = base_ops.get_account(user.id)
    assert account_user.balance == 1200.0


def test_withdrawal(user):
    do_withdrawal(600, account="296318745086616949474749325034555106571")
    base_ops = BaseOps()
    account_user = base_ops.get_account(user.id)
    assert account_user.balance == 600.0


def test_unique_account_per_user():
    base_ops = BaseOps()
    result = base_ops.create_new_register_account(account_user="test-name")
    assert (
        result
        == "Account for this costumer already exists, account number: 296318745086616949474749325034555106571"
    )


def test_record_extract():
    operation = OperationsAccount()
    result = operation.get_extract("296318745086616949474749325034555106571")
    assert len(result) == 2
