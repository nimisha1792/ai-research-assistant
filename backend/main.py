from fastapi import FastAPI
import asyncio
from database.database import engine, Base

# Import model so SQLAlchemy knows it exists
from models.note import Note
from routes.notes import router as notes_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(notes_router)

@app.get("/")
async def home():
    await asyncio.sleep(2)
    return {"message": "Async FastAPI Working"}

@app.get("/search")
async def search_notes(query: str):
    return {
        "search": query
    }

@app.get("/error")
async def error_demo():
    raise Exception("Something went wrong")