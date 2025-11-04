from fastapi import FastAPI
from app.routes import users, products, orders

app = FastAPI(title="API Viña Urbana", version="1.0")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/health")
def health():
    return {"status": "ok"}