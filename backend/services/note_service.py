notes = []
def get_all_notes():
    return notes

def create_new_note(note):
    notes.append(note.dict())
    return {
        "message": "Note created successfully",
        "data": note
    }