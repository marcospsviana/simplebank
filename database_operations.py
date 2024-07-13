from datetime import datetime, timezone
from uuid import uuid4

from psycopg2 import connect
from sqlmodel import Session, select

from models import Account, Extract, LimitWithDrawal, User, get_engine


def generate_account_number():
    number = uuid4()
    return number.int


def generate_extract_number(account):
    return int(account) + uuid4().int


class BaseOps:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = Session(self.engine)
        self.conn = connect(dsn="postgresql://postgres:postgres@localhost/postgres")
        self.cursor = self.conn.cursor()

    def create_new_register_user(self, name, citzen_id):
        try:
            self.session.add(User(name=name, citzen_id=citzen_id))
            self.session.commit()
        except Exception as err:
            print(f"User with citzen id already exists {err}")

    def get_user(self, name):
        statement = select(User).where(User.name == name)
        results = self.session.exec(statement)
        user = results.first()
        return user

    def update_user(self, name, new_name, nickname):
        statement = select(User).where(User.name == name)
        results = self.session.exec(statement)
        user = results.first()
        if new_name:
            user.name = new_name
        if nickname:
            user.nickname = nickname
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as err:
            print(f"Erro ao criar usuário {err}")

    def create_new_register_account(self, account_user, type=None, balance=None):
        account_number = generate_account_number()
        statement = select(User).where(User.name == account_user)
        results = self.session.exec(statement)
        user = results.one()
        account_statement = select(Account).where(Account.account_user == user.id)
        results = self.session.exec(account_statement)
        account_found = results.first()
        if account_found:
            return f"Account for this costumer already exists, account number: {account_found.account_number}"
        else:
            id_user = user.id
            account_user = int(id_user)
            type = type
            created_date = datetime.now()
            balance = balance
            account = Account(
                id=None,
                account_number=account_number,
                account_user=account_user,
                type=type,
                created_date=created_date,
                balance=balance,
            )
            self.session.add(account)
            self.session.commit()
            withdrawal_limit = LimitWithDrawal(
                id=None,
                account=account.id,
                withdrawal_day_limit=0,
                date_withdrawal=datetime.now(timezone.utc),
            )
            self.session.add(withdrawal_limit)
            self.session.commit()
            return f"Account {account_number} created successful!"

    def get_account(self, user):
        statement = select(Account).where(User.id == user)
        results = self.session.exec(statement)
        account = results.one()
        self.session.flush(account)
        return account


class OperationsAccount:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = Session(self.engine)

    def deposit(self, account, value):
        if float(value) < 0:
            return f"This value $ {value} is not allowed!"
        statement = select(Account).where(Account.account_number == account)
        results = self.session.exec(statement)
        account = results.one()
        account.balance += value
        self.session.add(account)
        self.session.commit()
        self.session.flush(account)
        self.do_record_extract(account, value, "deposit")

    def withdrawal(self, account, value):
        statement = select(Account).where(Account.account_number == account)
        results = self.session.exec(statement)
        account = results.first()
        if value > account.balance:
            return f"Account doesn't have enough to withdrawal $ {float(value)}, account balance: $ {account.balance}"
        else:
            limit_count_statement = select(LimitWithDrawal).where(
                LimitWithDrawal.account == account.id
            )
            result_count = self.session.exec(limit_count_statement)
            count = result_count.first()
            if count.withdrawal_day_limit == 3:
                return "You already have made three withdrawals today this is the limit daily!"
            account.balance -= value
            self.session.add(account)
            count.withdrawal_day_limit += 1
            self.session.add(count)
        self.session.add(account)
        self.session.commit()
        self.session.flush(account)
        self.do_record_extract(account, value, "withdrawal")
        return f"Withdrawal of value $ {float(value)} successful!"

    def get_extract(self, account):
        statement = select(Extract).where(Account.account_number == account)
        results = self.session.exec(statement)
        extract = results.all()
        return extract

    def do_record_extract(self, account, value, type_operation):
        extract = Extract(
            id=None,
            extract_number=generate_extract_number(account.account_number),
            account=account.id,
            value_operation=value,
            type_operation=type_operation,
            date_operation=datetime.now(timezone.utc),
        )
        self.session.add(extract)
        self.session.commit()
