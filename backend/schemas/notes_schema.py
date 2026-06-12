from pydantic import BaseModel

class Note(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    message: str
    data: Note

class NoteUpdate(BaseModel):
    title: str
    content: str