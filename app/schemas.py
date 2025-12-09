# =====================================
# app/schemas.py
# =====================================
from pydantic import BaseModel


class Note(BaseModel):
    id: int | None = None
    artist: str
    title: str
