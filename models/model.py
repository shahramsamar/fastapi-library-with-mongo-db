from pydantic import BaseModel



class Book(BaseModel):
    title: str
    authir: str
    