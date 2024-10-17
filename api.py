from fastapi import FastAPI

from .database_operations import BaseOps

app = FastAPI()

bo = BaseOps()


@app.get("/")
async def list_accounts():
    accounts = bo.get_all_data()

    return {"accounts": dict(accounts)}
