from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(2)
    return {"message": "Async FastAPI Working"}