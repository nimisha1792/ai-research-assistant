from sqlalchemy.orm import Session

from models.note import Note

def get_all_notes(db:Session):
    return db.query(Note).all()

def create_new_note(db:Session,note):
    db_note= Note(title=note.title,content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return {
        "message": "Note created successfully",
        "data": db_note
    }