from models import User, Account
from decimal import Decimal, Context
from database_operations import OperationsAccount
def do_withdrawal(value): ...


def do_deposit(value, account):
    operations = OperationsAccount()
    operations.deposit(account, value=value)


def get_extract(value): ...


def get_balance(value): ...
