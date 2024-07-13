from database_operations import OperationsAccount

operations = OperationsAccount()


def do_withdrawal(value, account):
    result = operations.withdrawal(account, value=value)
    return result


def do_deposit(value, account):
    result = operations.deposit(account, value=value)
    return result


def get_extract(account):
    operations.deposit(account)


def get_balance(account):
    operations.get_balance(account)
