from fastapi import FastAPI
from app.server.routes.account import router as AccountRouter
from app.server.database import init_db

app = FastAPI()

app.include_router(AccountRouter, tags=["Account"], prefix="/account")

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}