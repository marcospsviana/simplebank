from decimal import Context, Decimal

from database_operations import OperationsAccount
from models import Account, User


def do_withdrawal(value): ...


def do_deposit(value, account):
    operations = OperationsAccount()
    operations.deposit(account, value=value)


def get_extract(value): ...


def get_balance(value): ...
