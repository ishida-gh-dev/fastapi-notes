# FastAPI Notes API

A simple Notes API built with **FastAPI**, created as part of a technical portfolio submission.

## 📌 Features

-   Create, read, update, delete notes (CRUD)
-   FastAPI with auto-generated Swagger UI
-   Simple in-memory data store (for demonstration)
-   Fully typed Python code

## 🛠 Tech Stack

-   Python 3.11
-   FastAPI
-   Uvicorn
-   Pydantic

## 🚀 How to run (local)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

-   Access Swagger UI:
    http://localhost:8000/docs

## 📄 Endpoints

-   GET /notes
-   POST /notes
-   GET /notes/{id}
-   PUT /notes/{id}
-   DELETE /notes/{id}

## 🎯 Purpose

This project was created to demonstrate basic backend API development skills using FastAPI.

## 📬 Contact

ishida-gh-dev
