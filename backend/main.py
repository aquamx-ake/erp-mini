
from fastapi import FastAPI
from routers import customers, products, invoices
from database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(customers.router)
app.include_router(products.router)
app.include_router(invoices.router)

@app.get("/health")
def health():
    return {"ok": True}
