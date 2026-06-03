from fastapi import APIRouter
from schemas.notes_schema import Note, NoteResponse
from services.note_service import get_all_notes, create_new_note
from fastapi import HTTPException

router = APIRouter()

@router.get("/notes")
async def get_notes():
    return {
        "message": "Notes retrieved successfully",
        "data": get_all_notes()
    }

@router.post("/notes", response_model=NoteResponse)
async def create_note(note: Note): 
    return create_new_note(note)

@router.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    notes = get_all_notes()

    if note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    deleted = notes.pop(note_id)
    return {
        "message": "Note deleted successfully",
        "data": deleted
    }