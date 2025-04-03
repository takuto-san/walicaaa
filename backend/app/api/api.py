"""
app/api/api.py
エンドポイントのルーターを統合
"""
from fastapi import APIRouter
from app.api.endpoints import event

api_router = APIRouter()

api_router.include_router(event.router, prefix="/event", tags=["event"])
