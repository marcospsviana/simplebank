from datetime import datetime, timezone
from enum import Enum

from sqlmodel import Field, SQLModel, create_engine


def get_engine():
    engine = create_engine(
        "postgresql://postgres:postgres@localhost/postgres",
        isolation_level="REPEATABLE READ",
    )
    return engine


class TypeAccount(Enum):
    BASIC_ACCOUNT = "basic"
    CHECKING_ACCOUNT = "checking"


class User(SQLModel, table=True):
    id: int | None = Field(
        default=None, primary_key=True, unique=True, unique_items=True
    )
    name: str
    citzen_id: str = Field(unique=True, unique_items=True)


class Account(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, unique=True)
    account_number: str = Field(unique=True)
    account_user: int = Field(foreign_key="user.id", unique_items=True)
    type: TypeAccount = Field(default=TypeAccount.BASIC_ACCOUNT)
    created_date: datetime = Field(default=datetime.now(timezone.utc), nullable=False)
    balance: float = Field(default=0)

    def __repr__(self) -> str:
        return f"{self.account_number}"


class Address(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, unique=True)
    user: int = Field(foreign_key="user.id", nullable=False)
    address_number: str = Field(nullable=False)
    city: str = Field(nullable=False)
    state: str = Field(nullable=False, max_length=3)


if __name__ == "__main__":
    engine = get_engine()
    SQLModel.metadata.create_all(engine)
