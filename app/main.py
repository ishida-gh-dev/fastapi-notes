# =====================================
# app/main.py
# =====================================
from fastapi import FastAPI
from app.routers import notes


app = FastAPI(title="FastAPI Notes API")


app.include_router(notes.router)
