from fastapi import FastAPI, HTTPException
import random
import json
import os
from pydantic import BaseModel
from typing import Optional, Literal
from uuid import uuid4
from fastapi.encoders import jsonable_encoder

app = FastAPI()

BOOK_FILE = "book.json"
BOOK_DATABASE = []

class Book(BaseModel):
    name: str
    price: float
    genre: Literal["fiction", "non-fiction"]
    book_id: Optional[str] = None

# Load books from file if it exists
if os.path.exists(BOOK_FILE):
    with open(BOOK_FILE, "r") as f:
        try:
            books_data = json.load(f)
            BOOK_DATABASE = [Book(**book) for book in books_data]
        except (json.JSONDecodeError, TypeError):
            BOOK_DATABASE = []  # Reset database if JSON file is invalid

@app.get("/")
async def home():
    return {"Message": "Welcome to Book Store"}

@app.get("/list-book")
async def list_book():
    return {"books": BOOK_DATABASE}

@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        raise HTTPException(404, f"Index {index} is out of range. Total books: {len(BOOK_DATABASE)}")
    return jsonable_encoder(BOOK_DATABASE[index])  # Ensure JSON compatibility

@app.get("/get-random-book")
async def get_random_book():
    if not BOOK_DATABASE:
        raise HTTPException(404, "No books available in the database.")
    return jsonable_encoder(random.choice(BOOK_DATABASE))

@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex  # Assign unique book_id
    BOOK_DATABASE.append(book)

    with open(BOOK_FILE, "w") as f:
        json.dump(jsonable_encoder(BOOK_DATABASE), f, indent=4)

    return {"message": f"New book '{book.name}' is added to the database.", "book_id": book.book_id}

@app.get('/get-book')
async def get_book(book_id: str):
    for book in BOOK_DATABASE:
        if book.book_id == book_id:
            return jsonable_encoder(book)  # Ensure JSON serialization
    raise HTTPException(404, f"Book not found: {book_id}")
