# =====================================
# app/routers/notes.py
# =====================================
from fastapi import APIRouter, HTTPException
from app.schemas import Note


router = APIRouter(prefix="/notes", tags=["Notes"])


notes_db: list[Note] = []


@router.get("/")
def list_notes():
    return notes_db


@router.post("/")
def create_note(note: Note):
    note.id = 1 if not notes_db else notes_db[-1].id + 1
    notes_db.append(note)
    return note


@router.get("/{note_id}")
def get_note(note_id: int):
    for note in notes_db:
        if note.id == note_id:
            return note
        raise HTTPException(status_code=404, detail="Note not found")


@router.put("/{note_id}")
def update_note(note_id: int, updated: Note):
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            updated.id = note_id
            notes_db[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Note not found")


@router.delete("/{note_id}")
def delete_note(note_id: int):
    for index, note in enumerate(notes_db):
        if note.id == note_id:
            del notes_db[index]
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Note not found")
