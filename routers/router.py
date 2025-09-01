from fastapi import APIRouter
from models.model import Book
from configurations.database import books_collection



MyRouter = APIRouter()




@MyRouter.get("/")
async def book_list():
    books = list(books_collection.find({},{"_id":0}))
    return {"books":books}
    


@MyRouter.post("/")
async def add_book(book:Book):
    book_single = book.dict()
    books_collection.insert_one(book_single)
    return {"message":"Book added successfully"}


@MyRouter.get("/book/{title}")
async def get_book_by_title(title:str):
    book = books_collection.find_one({"title":title},{"_id":0})
    if book:
        return {"book":book}
    return {"message":"Book not found"}


@MyRouter.put("/update_book/{title}")
async def update_book(title:str, updated_book:Book):
    result = books_collection.update_one(
        {"title":title},
        {"$set":updated_book.dict()}
    )
    if result.modified_count:
        return {"message":"Book updated succeefully"}
    return {"message":"Book not found or not updated"}    