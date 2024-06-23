import pytest
import sqlite3
from sqlmodel import SQLModel, create_engine
from models import User



@pytest.fixture
def db_session_test():
    connection = sqlite3.connect(":memory:")
    # SQLModel.metadata.create_all(connection)
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
def user(db_session_test):
    user = User("test-name", "test")
    yield user
