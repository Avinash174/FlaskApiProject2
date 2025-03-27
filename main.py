from fastapi import FastAPI
app=FastAPI()

BOOK_DATABASE=[
    "Great Minds",
    "Rech Dad Poor Dad",
    "Atomic Habits",
    "The Great Gatsby"
]

# /

@app.get("/")
async def home():
    return{"Meassage":"Welcome Book Store"}

#/list-book

@app.get("/list-book")
async def list_book():
    return {"book":[]}
#book-by-index/{index}

#/get-random-book

#/add-book

#/get-book?id=....