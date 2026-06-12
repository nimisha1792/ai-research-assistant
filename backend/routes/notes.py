from fastapi import APIRouter, Depends
from schemas.notes_schema import Note, NoteResponse, NoteUpdate
from services.note_service import get_all_notes, create_new_note, update_note, delete_note
from fastapi import HTTPException
from database.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/notes")
async def get_notes(db: Session = Depends(get_db)):
    return {
        "message": "Notes retrieved successfully",
        "data": get_all_notes(db)
    }


@router.post("/notes", response_model=NoteResponse)
async def create_note(note: Note,   db: Session = Depends(get_db)):
    return create_new_note(db, note)


@router.put("/notes/{note_id}")
async def update_note_route(
    note_id: int,
    updated_note: NoteUpdate,
    db: Session = Depends(get_db)
):
    note = update_note(
        db,
        note_id,
        updated_note
    )
    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    return {
        "message": "Note updated successfully",
        "data": note
    }


@router.delete("/notes/{note_id}")
async def delete_note_route(
    note_id: int,
    db: Session = Depends(get_db)
):
    note = delete_note(
        db,
        note_id
    )
    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    return {
        "message": "Note deleted successfully",
        "data": note
    }
