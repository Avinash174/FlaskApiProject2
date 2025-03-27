from fastapi import FastAPI,HTTPException
import random
app=FastAPI()

BOOK_DATABASE=[
    "Great Minds",
    "Rech Dad Poor Dad",
    "Atomic Habits",
    "The Great Gatsby",
    "Indian Great Man"
]

# /

@app.get("/")
async def home():
    return{"Meassage":"Welcome Book Store"}

#/list-book

@app.get("/list-book")
async def list_book():
    return {"books":BOOK_DATABASE}

#book-by-index/{index}

@app.get("/book-by-index/{index}")
async def book_by_index(index:int):
    if index <0 or index >=len(BOOK_DATABASE):
        raise HTTPException(404,f"Index{index} is out of range{len(BOOK_DATABASE)}")
    else:
        return {"books":BOOK_DATABASE[index]}

#/get-random-book

@app.get('/get-random-book')
async def get_random_book():
    return random.choice(BOOK_DATABASE)
    

#/add-book

# GET , POST , PATCH , PUT , DELETE   - Api methods

#/get-book?id=....