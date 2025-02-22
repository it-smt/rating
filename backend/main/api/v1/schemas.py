from ninja import Schema
from pydantic import BaseModel


class SDriverShow(BaseModel):
    """Схема для водителя."""

    id: int
    name: str | None
    call_sign: str
    orders_count: int
    rank: str
    grade: str


class SMsg(Schema):
    """Схема для сообщения."""

    msg: str
