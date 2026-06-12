from sqlalchemy.orm import Session

from models.note import Note


def get_all_notes(db: Session):
    return db.query(Note).all()


def create_new_note(db: Session, note):
    db_note = Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return {
        "message": "Note created successfully",
        "data": db_note
    }


def update_note(db: Session, note_id: int, updated_note):
    note = (db.query(Note).filter(Note.id == note_id).first())
    if not note:
        return None
    note.title = updated_note.title
    note.content = updated_note.content
    db.commit()
    db.refresh(note)
    return note


def delete_note(
    db: Session,
    note_id: int
):

    note = (
        db.query(Note)
        .filter(Note.id == note_id)
        .first()
    )

    if not note:
        return None
    db.delete(note)
    db.commit()
    return note
