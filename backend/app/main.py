"""
app/main.py
FastAPIアプリケーションのエントリーポイント
"""
from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Hello from the split payment app"}
