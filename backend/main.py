from fastapi import FastAPI
import asyncio
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()
notes = []

class Note(BaseModel):
    title: str
    content: str

@app.get("/")
async def home():
    await asyncio.sleep(2)
    return {"message": "Async FastAPI Working"}

@app.get("/notes/{note_id}")
async def get_note(note_id: int):
    if note_id > len(notes):
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    return notes[note_id - 1]

@app.post("/notes")
async def create_note(note: Note):
    notes.append(note.dict())
    return {"message": "Note created successfully", "note": note}

@app.get("/search")
async def search_notes(query: str):
    return {
        "search": query
    }

@app.get("/error")
async def error_demo():
    raise Exception("Something went wrong")