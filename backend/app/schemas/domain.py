"""
app/schemas/domain.py
ドメインモデルのスキーマ定義
User, Asset, Debt, Payment, Event を Pydantic で定義
"""
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: str
    name: str

class Asset(BaseModel):
    price: int
    owner: User

class Debt(BaseModel):
    price: int
    debtor: User

class Payment(BaseModel):
    id: str
    price: int
    payer: User
    payees: List[User]

class Event(BaseModel):
    id: str
    users: List[User]
    payments: List[Payment]
