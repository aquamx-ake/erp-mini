from fastapi import FastAPI
from routers import customers, products, invoices
from database import init_db

app = FastAPI(title="ERP mini", version="0.1.0")

# สร้างตารางครั้งแรกตอนแอปรันขึ้น
@app.on_event("startup")
def on_startup():
    init_db()

# เส้นหลักให้ Render เช็คตอน deploy (กัน timeout)
@app.get("/")
def root():
    return {"message": "ERP-mini is running!"}

# health check ใช้เช็คสถานะ
@app.get("/health")
def health():
    return {"ok": True}

# รวม router ย่อย ๆ
app.include_router(customers.router)
app.include_router(products.router)
app.include_router(invoices.router)
