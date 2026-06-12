# AI Research Assistant

Documenting my transition from frontend/mobile engineering into AI product engineering.

Topics being explored:
- Python
- FastAPI
- Docker
- RAG systems
- Vector databases
- AI workflows
- Async systems
- LLM applications

Goal:
Build scalable AI-powered backend systems while learning modern AI engineering concepts.

AI Research Assistant

Backend application built using FastAPI and SQLAlchemy as part of a learning journey toward building a Research Intelligence Platform.

Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

⸻

Clone Repository

git clone <repo-url>
cd ai-research-assistant/backend

⸻

Create Virtual Environment

python3 -m venv venv

Activate:

Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate

⸻

Install Dependencies

pip install -r requirements.txt

⸻

Run Application

uvicorn main:app --reload

⸻

Open Swagger UI

http://127.0.0.1:8000/docs

⸻

Project Structure

backend/
├── database/
├── models/
├── routes/
├── schemas/
├── services/
├── main.py
├── requirements.txt
└── README.md

⸻

Current Features

* FastAPI REST APIs
* SQLAlchemy ORM
* SQLite Database
* Dependency Injection
* CRUD Architecture

⸻

Roadmap

Phase 1

* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker

Phase 2

* Document Management

Phase 3

* Hybrid Search

Phase 4

* AI Research Assistant

Phase 5

* Research Intelligence Platform

:::
---
# What I Want You To Do Before Anything Else
1. Generate `requirements.txt`
```bash
pip freeze > requirements.txt

2. Create .gitignore
3. Create README.md
4. Commit

git add .
git commit -m "Add project setup documentation and dependencies"
git push

This is exactly the kind of engineering hygiene that makes a project feel professional instead of experimental.