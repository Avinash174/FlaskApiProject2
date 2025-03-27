from fastapi import FastAPI, HTTPException
import random
import json
import os

app = FastAPI()

BOOK_FILE = "book.json"
BOOK_DATABASE = [
    "Great Minds",
    "Rich Dad Poor Dad",
    "Atomic Habits",
    "The Great Gatsby",
    "Indian Great Man"
]

# Load books from file if it exists

if os.path.exists(BOOK_FILE):
    with open(BOOK_FILE, "r") as f:
        BOOK_DATABASE = json.load(f)

# Home Route
@app.get("/")
async def home():
    return {"Message": "Welcome to Book Store"}

# List all books
@app.get("/list-book")
async def list_book():
    return {"books": BOOK_DATABASE}

# Get book by index
@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        raise HTTPException(404, f"Index {index} is out of range. Total books: {len(BOOK_DATABASE)}")
    return {"book": BOOK_DATABASE[index]}

# Get a random book
@app.get("/get-random-book")
async def get_random_book():
    return {"book": random.choice(BOOK_DATABASE)}

# Add a new book

# GET , POST , PATCH , PUT , DELETE   - Api methods

@app.post("/add-book")
async def add_book(book: str):
    BOOK_DATABASE.append(book)
    return {"message": f"New book '{book}' is added to the database"}

#/get-book?id=....