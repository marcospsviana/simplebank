import pytest
import freezegun
from datetime import datetime
import sqlite3
from sqlmodel import SQLModel, create_engine, Session, select
from models import User, Account, TypeAccount
from pytest_postgresql import factories
import psycopg2
from database_operations import BaseOps


from pytest_postgresql.janitor import DatabaseJanitor

# @pytest.fixture
# def database(postgresql_proc):
#     # variable definition

#     with DatabaseJanitor(
#         postgresql_proc.user,
#         postgresql_proc.host,
#         postgresql_proc.port,
#         "my_test_database",
#         postgresql_proc.version,
#         password="secret_password",
#     ):
#         yield psycopg2.connect(
#             dbname="my_test_database",
#             user=postgresql_proc.user,
#             password="secret_password",
#             host=postgresql_proc.host,
#             port=postgresql_proc.port,
        # )
@pytest.fixture
def session():
    engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)
    session = Session(engine)
    yield session




    

@pytest.fixture
def user(session):
    # session.add(User(name="test-name", citzen_id="123456789"))
    # session.commit()
    base_ops = BaseOps()
    base_ops.create_new_register_user(name="test-name", citzen_id="123456789")
    session.flush(User)
    statement = select(User).where(User.name == "test-name")
    results = session.exec(statement)
    user = results.one()
    yield user
    session.delete(user)

# @pytest.mark.freeze_time(datetime(2024, 6, 23, 23, 18, 55, 529419))
@pytest.fixture
def account(user, freezer, session):
    base_ops = BaseOps()
    base_ops.create_new_register_account(account_user=user.name, type=TypeAccount.BASIC_ACCOUNT, balance=0)
    # session.commit()
    session.flush(Account)
    statement = select(Account).where(Account.account_user==user.id)
    results = session.exec(statement)
    account = results.one()
    yield account
    session.delete(account)

