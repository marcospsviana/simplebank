from typing import Any, Dict, Optional, Tuple
from enum import Enum
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, create_engine
from decimal import Decimal


class TypeAccount(Enum):
    BASIC_ACCOUNT = "basic"
    CHECKING_ACCOUNT = "checking"


class User(SQLModel, table=True):
    def __init__(self, name=None, nickname=None):
        self.name = name
        self.nickname = nickname
    id: int = Field(primary_key=True)
    name: str
    nickname: Optional[str]


class Account(SQLModel, table=True):
    def __init__(self, account_number=None, account_user=None, type=None, created_date=None, balance=None):
        self.account_number=account_number
        self.account_user=account_user
        self.type=type
        self.created_date=created_date
        self.balance=balance
    id: int = Field(primary_key=True)
    account_number: str
    account_user: int = Field(foreign_key="user.id")
    type: TypeAccount = Field(default=TypeAccount.BASIC_ACCOUNT)
    created_date: datetime = Field(default=datetime.now(timezone.utc), nullable=False)
    balance: Decimal = Field(decimal_places=2, default=0)


class Address(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user: int = Field(foreign_key="user.id", nullable=False)
    address_number: str = Field(nullable=False)
    city: str = Field(nullable=False)
    state: str = Field(nullable=False, max_length=3)


if __name__ == "__main__":
    engine = create_engine("sqlite:///bank.db", echo=True)
    SQLModel.metadata.create_all(engine)
