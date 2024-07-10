
from database_operations import OperationsAccount


def do_withdrawal(value, account):
    operations = OperationsAccount()
    operations.withdrawal(account, value=value)


def do_deposit(value, account):
    operations = OperationsAccount()
    operations.deposit(account, value=value)


def get_extract(value): ...


def get_balance(value): ...
