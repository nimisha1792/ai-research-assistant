# Python & FastAPI Foundations — Learning Summary

## Background

As an experienced React Native and JavaScript engineer transitioning into AI product engineering, the focus of learning Python is not just syntax.

The focus is:
- backend systems
- execution understanding
- async programming
- AI infrastructure foundations
- scalable API development

This journey is being approached from a software engineering perspective rather than beginner programming tutorials.

---

# Python Mental Model

One of the most important realizations:

## Variables are references to objects

Python variables do not directly store values.

They reference objects in memory.

Example:

python id="r1" a = [1, 2] b = a  b.append(3)  print(a) 

Output:

python id="r2" [1, 2, 3] 

Both variables point to the same object.

This becomes extremely important in:
- backend systems
- request handling
- async programming
- state mutation
- AI pipelines

---

# Mutable vs Immutable Objects

## Mutable Objects
Can change in-place.

Examples:
- list
- dict
- set

python id="r3" nums = [1, 2] nums.append(3) 

---

## Immutable Objects
Cannot change after creation.

Examples:
- int
- str
- tuple

python id="r4" name = "Nimisha"  another = name  another += " Anand" 

Python creates a NEW object instead of modifying the original string.

---

# Shallow Copy vs Deep Copy

## Assignment

python id="r5" b = a 

No new object created.
Both variables reference same object.

---

## Shallow Copy

python id="r6" b = a.copy() 

Creates new outer object.

Nested objects remain shared.

---

## Deep Copy

python id="r7" import copy  b = copy.deepcopy(a) 

Recursively copies everything.

This is very important in nested backend payloads and AI data transformations.

---

# Python Collections

## List

Equivalent to JavaScript arrays.

python id="r8" nums = [1, 2, 3] 

Properties:
- ordered
- mutable
- duplicates allowed

Used heavily in:
- APIs
- AI chunking
- batching
- pipelines

---

## Tuple

Immutable ordered collection.

python id="r9" point = (10, 20) 

Useful for:
- coordinates
- fixed structures
- cache keys

---

## Set

Unique unordered collection.

python id="r10" nums = {1, 2, 3} 

Main advantage:
- extremely fast lookup

Used for:
- deduplication
- caching
- permission checks
- graph traversal

---

## Dictionary

Key-value data structure.

python id="r11" user = {     "name": "Nimisha",     "skills": ["React", "Python"] } 

Used everywhere in:
- JSON APIs
- metadata
- backend payloads
- AI responses

---

# Functions in Python

Functions are:
# first-class objects

Meaning:
- functions can be stored in variables
- passed as arguments
- returned from other functions

Example:

python id="r12" def greet(name):     return f"Hello {name}"  say_hi = greet 

This concept becomes foundational for:
- decorators
- FastAPI
- middleware
- async systems
- AI orchestration

---

# Stack Frames & Execution Flow

When a function executes:
- Python creates stack frame
- local variables stored
- execution happens
- frame destroyed after return

Execution flow understanding is important for:
- recursion
- debugging
- async systems
- backend tracing

---

# Python Execution Internals

High-level execution flow:

text id="r13" Python Source Code ↓ Bytecode Compilation ↓ Python Virtual Machine ↓ Execution 

Important concepts:
- CPython
- bytecode
- interpreter
- execution model

---

# GIL (Global Interpreter Lock)

One of Python’s most important concurrency concepts.

In CPython:
# only one thread executes Python bytecode at a time

This affects:
- threading
- concurrency
- backend scaling

---

# Concurrency vs Parallelism

## Concurrency
Handling multiple tasks efficiently.

Example:
- APIs
- DB calls
- AI requests

---

## Parallelism
True simultaneous CPU execution.

Usually achieved using:
- multiple processes
- multiple cores

---

# Async / Await

One of the most important backend concepts.

Example:

python id="r14" import asyncio  async def task():     await asyncio.sleep(2) 

await means:

# “Pause this coroutine while waiting and allow other work to continue.”

This creates:
- non-blocking execution
- scalable APIs
- efficient request handling

---

# Event Loop

Async systems are managed by:
# event loop

Responsibilities:
- scheduling coroutines
- pausing waiting tasks
- resuming execution

Very similar conceptually to JavaScript event loop.

---

# Async Concurrency

Example:

python id="r15" await asyncio.gather(task1(), task2()) 

Allows multiple coroutines to run concurrently.

This is extremely important for:
- AI APIs
- OpenAI calls
- vector DB retrieval
- streaming responses
- WebSockets

---

# Why FastAPI Became Popular

FastAPI is:
# async-first

Advantages:
- high performance
- clean API development
- automatic validation
- modern Python typing
- excellent for AI backends

---

# FastAPI Fundamentals

Basic API example:

python id="r16" from fastapi import FastAPI  app = FastAPI()  @app.get("/") async def home():     return {"message": "Hello"} 

---

# GET vs POST

## GET
Used for fetching data.

python id="r17" @app.get("/notes") 

---

## POST
Used for creating data.

python id="r18" @app.post("/notes") 

---

# Pydantic Validation

FastAPI uses:
# Pydantic

for request validation.

Example:

python id="r19" from pydantic import BaseModel  class Note(BaseModel):     title: str     content: str 

Benefits:
- automatic validation
- type safety
- cleaner backend architecture

---

# Request Lifecycle

High-level backend request flow:

text id="r20" Client Request ↓ FastAPI Route ↓ Validation ↓ Function Execution ↓ Response 

This is foundational backend architecture understanding.

---

# Current Direction

Current focus areas:
- Python internals
- FastAPI
- async systems
- backend architecture
- AI engineering foundations

Goal:
Build scalable AI-powered backend systems while transitioning from frontend/mobile engineering into AI product engineering.

---

# Key Engineering Takeaways

Important learnings so far:
- Python variables are references
- mutability matters deeply
- async is critical for modern APIs
- FastAPI aligns naturally with AI systems
- backend engineering is heavily I/O-focused
- Python excels at orchestration and developer productivity

This learning path is being approached through:
- building projects
- backend APIs
- GitHub documentation
- LinkedIn technical writing
- AI-focused engineering systems