from database_operations import OperationsAccount

operations = OperationsAccount()


def do_withdrawal(value, account):
    result = operations.withdrawal(account, value=value)
    return result


def do_deposit(value, account):
    result = operations.deposit(account, value=value)
    return result


def get_extract(account):
    result = operations.get_extract(account)
    text = f"\n ============== extract account {account} ============== \n"
    for r in result:
        text += f"extract number: {r['extract_number']}\n"
        text += f"type_operation: {r['type_operation']}\n"
        text += f"date: {r['date_operation']}\n"
        text += f"value: $ {r['value_operation']}\n"
        text += "--------------------------------------------\n"
    return text


def get_balance(account):
    operations.get_balance(account)
