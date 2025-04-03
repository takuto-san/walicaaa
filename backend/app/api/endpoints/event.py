"""
app/api/endpoints/event.py
割り勘イベントのエンドポイント
GET /event/ でダミーデータのイベント情報を返す
"""
from fastapi import APIRouter
from app.schemas.domain import Event, Payment, User

router = APIRouter()

@router.get("/", response_model=Event)
def get_dummy_event():
    alice = User(id="u1", name="Alice")
    bob = User(id="u2", name="Bob")
    payment = Payment(id="p1", price=100, payer=alice, payees=[bob])
    
    event = Event(id="e1", users=[alice, bob], payments=[payment])
    return event
