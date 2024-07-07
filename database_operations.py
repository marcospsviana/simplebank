from datetime import datetime
from uuid import uuid4

from psycopg2 import connect
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, exists, insert, select, update

from models import Account, Address, User, get_engine


class BaseOps:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = Session(self.engine)
        self.conn = connect(dsn="postgresql://postgres:postgres@localhost/postgres")
        self.cursor = self.conn.cursor()
        


    def create_new_register_user(self, name, citzen_id):
        self.session.add(User(name=name, citzen_id=citzen_id))
        self.session.commit()
        
        
        
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
            print(f'Erro ao criar usuário {err}')
    
    def create_new_register_account(self, account_user, type=None, balance=None):
        account_number = generate_account_number()
        statement = select(User).where(User.name == account_user)
        results = self.session.exec(statement)
        user = results.one()
        id_user = user.id
        account_user = int(id_user)
        type=type
        created_date = datetime.now()
        balance=balance
        account = Account(id=None,account_number=account_number, account_user=account_user, type=type, created_date=created_date, balance=balance)
        try:
            self.session.add(account)
            self.session.commit()
        except Exception as err:
            print(f'Errou {err}')
    
    def get_account(self, user):
        statement = select(Account).where(User.id == user)
        results = self.session.exec(statement)
        account = results.one()
        return account


class OperationsAccount:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = Session(self.engine)
    
    def deposit(self, account, value):
        statement = select(Account).where(Account.account_number == account)
        results = self.session.exec(statement)
        account = results.one()
        account.balance += value
        # update_statement = update(Account).where(Account.account_number == account).values(balance = value)
        # self.session.exec(update_statement)
        self.session.add(account)
        self.session.commit()
        self.session.flush(account)



def generate_account_number():
        number = uuid4()
        return number.int

