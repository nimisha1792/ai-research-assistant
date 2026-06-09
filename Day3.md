Here’s the README for Today’s Learning (Database + SQLAlchemy + FastAPI Integration). This is the one I’d actually commit to GitHub.

Day 3 – Database Integration with FastAPI & SQLAlchemy

Objective

The goal of today’s session was to move from temporary in-memory storage to a persistent database-backed backend architecture.

Before today, notes were stored in a Python list:

notes = []

This meant all data was lost whenever the server restarted.

Today we introduced:

* SQL fundamentals
* SQLite
* SQLAlchemy ORM
* Database models
* Sessions
* Dependency Injection
* FastAPI ↔ SQLAlchemy integration

⸻

Why We Need Databases

Using:

notes = []

has several limitations:

* Data is lost on server restart
* No persistence
* Not scalable
* Difficult to query efficiently
* Not suitable for multiple users

Databases solve these problems by providing:

* Persistent storage
* Querying capabilities
* Indexing
* Relationships
* Transactions
* Concurrency control

⸻

SQL Fundamentals

SQL (Structured Query Language) is the language used to interact with relational databases.

Read Data

SELECT * FROM notes;

Retrieve all notes.

⸻

Filter Data

SELECT *
FROM notes
WHERE id = 2;

Retrieve a specific note.

⸻

Insert Data

INSERT INTO notes (title, content)
VALUES ('Docker', 'Containers');

Create a new record.

⸻

Update Data

UPDATE notes
SET content = 'Docker Containers and Images'
WHERE id = 2;

Modify existing data.

⸻

Delete Data

DELETE FROM notes
WHERE id = 2;

Remove a record.

⸻

CRUD Mapping

Most backend systems revolve around CRUD operations.

Operation	SQL
Create	INSERT
Read	SELECT
Update	UPDATE
Delete	DELETE

Understanding CRUD is foundational for API development.

⸻

Primary Keys

A primary key uniquely identifies a record.

Example:

id INTEGER PRIMARY KEY

Benefits:

* Unique identifier
* Fast lookups
* Required for relationships

⸻

Database Relationships

Introduced the concept of:

One-to-One

User
↓
Profile

⸻

One-to-Many

User
↓
Many Notes

Most common relationship.

⸻

Many-to-Many

Student
↓
Courses

Students can have many courses and courses can have many students.

⸻

ORM (Object Relational Mapper)

Instead of writing raw SQL everywhere, an ORM maps:

Python Objects
↔
Database Tables

The ORM used today:

SQLAlchemy

Example:

db.query(Note).all()

instead of:

SELECT * FROM notes;

⸻

SQLite

For local development we used:

SQLite

Benefits:

* Lightweight
* File-based
* No separate server required
* Perfect for learning and prototyping

Database file:

notes.db

⸻

Database Configuration

Created:

database/database.py

Responsibilities:

* Database engine
* Session management
* Base model creation

Example:

DATABASE_URL = "sqlite:///./notes.db"

⸻

SQLAlchemy Engine

Engine acts as the connection layer between:

FastAPI
↓
SQLAlchemy
↓
SQLite

Created using:

create_engine(...)

⸻

Sessions

Sessions manage database interactions.

Typical lifecycle:

Open Session
↓
Run Queries
↓
Commit Changes
↓
Close Session

Created using:

SessionLocal

⸻

Dependency Injection

Implemented:

def get_db():

FastAPI uses dependency injection to automatically provide a database session to routes.

Example:

db: Session = Depends(get_db)

Flow:

Request
↓
Create Session
↓
Execute Route
↓
Close Session

This is a core FastAPI concept.

⸻

SQLAlchemy Models

Created:

models/note.py

Example:

class Note(Base):

This class represents a database table.

Mapping:

Python Class
↓
Database Table

⸻

Table Creation

Used:

Base.metadata.create_all(bind=engine)

This automatically generated:

notes table

inside:

notes.db

⸻

Service Layer Refactoring

Migrated from:

notes.append(...)

to:

db.add(...)
db.commit(...)
db.refresh(...)

⸻

Understanding Database Writes

Add

db.add(db_note)

Stages the object for insertion.

⸻

Commit

db.commit()

Persists changes permanently.

Equivalent to executing:

INSERT INTO notes (...)

⸻

Refresh

db.refresh(db_note)

Reloads the object from the database.

Useful for retrieving generated values such as:

id

⸻

Backend Architecture Achieved

Current architecture:

Client
↓
FastAPI Route
↓
Dependency Injection
↓
Service Layer
↓
SQLAlchemy ORM
↓
SQLite Database

This is a production-style backend architecture pattern.

⸻

Important Debugging Lessons

Encountered:

NameError

db is not defined

Cause:

Database session was not injected into route.

Solution:

db: Session = Depends(get_db)

⸻

Response Validation Error

FastAPI validates responses using Pydantic schemas.

Learned that:

SQLAlchemy Model
≠
Pydantic Schema

and both must be properly mapped.

This will be completed in the next session.

⸻

Key Takeaways

Important concepts learned today:

* Why databases exist
* SQL fundamentals
* CRUD operations
* Primary keys
* Relationships
* SQLite
* SQLAlchemy
* ORM architecture
* Sessions
* Dependency Injection
* FastAPI database integration
* Backend layering
* Real-world debugging

⸻

Current Backend Architecture

backend/
├── database/
│   └── database.py
│
├── models/
│   └── note.py
│
├── schemas/
│   └── notes_schema.py
│
├── services/
│   └── note_service.py
│
├── routes/
│   └── notes.py
│
└── main.py

⸻

Next Session

Topics planned:

* Fix Pydantic ↔ SQLAlchemy integration
* Complete persistent CRUD
* Database delete operation
* Response models
* SQLAlchemy relationships
* PostgreSQL introduction
* Database migrations
* Docker integration

At the end of this phase, the backend will evolve from a simple Notes API into a production-ready foundation for AI applications.
