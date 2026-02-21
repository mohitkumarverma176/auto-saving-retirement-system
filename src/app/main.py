from fastapi import FastAPI
from api import performance, transaction, returns


app = FastAPI(
    title="Auto saving retirement system API",
    version="1.0"
)

app.include_router(transaction.router, prefix="/transaction")
app.include_router(returns.router, prefix="/returns")
app.include_router(performance.router, prefix="/performance")