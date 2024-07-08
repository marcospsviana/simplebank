import sqlite3
from datetime import datetime

import freezegun
import psycopg2
import pytest
from pytest_postgresql import factories
from pytest_postgresql.janitor import DatabaseJanitor
from sqlmodel import Session, SQLModel, create_engine, select

from database_operations import BaseOps
from models import Account, TypeAccount, User


@pytest.fixture
def session():
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
    )
    session = Session(engine)
    yield session


@pytest.fixture
def user(session):
    base_ops = BaseOps()
    base_ops.create_new_register_user(name="test-name", citzen_id="123456789")
    session.flush(User)
    statement = select(User).where(User.name == "test-name")
    results = session.exec(statement)
    user = results.one()
    yield user
    session.delete(user)


@pytest.fixture
def account(user, freezer, session):
    base_ops = BaseOps()
    base_ops.create_new_register_account(
        account_user=user.name, type=TypeAccount.BASIC_ACCOUNT, balance=0
    )
    # session.commit()
    session.flush(Account)
    statement = select(Account).where(Account.account_user == user.id)
    results = session.exec(statement)
    account = results.one()
    yield account
    session.delete(account)
