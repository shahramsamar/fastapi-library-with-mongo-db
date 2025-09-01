from fastapi import FastAPI
from models.model import Book
from configurations.database import books_collection

app = FastAPI(debug=True)



@app.get("/")
async def book_list():
    books = list(books_collection.find({},{"_id":0}))
    return {"books":books}
    


@app.post("/")
async def add_book(book:Book):
    book_single = book.dict()
    books_collection.insert_one(book_single)
    return {"message":"Book added successfully"}


@app.get("/book/{title}")
def get_book_by_title(title:str):
    book = books_collection.find_one({"title":title},{"_id":0})
    if book:
        return {"book":book}
    return {"message":"Book not found"}

