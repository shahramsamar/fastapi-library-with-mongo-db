from fastapi import FastAPI
from models.model import Book
from configurations.database import books_collection

app = FastAPI(debug=True)



@app.get("/")
async def book_list():
    books = books_collection.find().to_list(length=10)
    return books
    


@app.post("/")
async def add_book(book:Book):
    book_single = book.dict()
    books_collection.insert_one(book_single)
    return {"message":"Book added successfully"}

