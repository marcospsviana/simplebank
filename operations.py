from database_operations import OperationsAccount

operations = OperationsAccount()


def do_withdrawal(value, account):
    operations.withdrawal(account, value=value)


def do_deposit(value, account):
    operations.deposit(account, value=value)


def get_extract(account):
    operations.deposit(account)


def get_balance(account):
    operations.get_balance(account)
