from pydantic import BaseModel

# Information on a book fetched from OpenLibrary
class Book(BaseModel):
    title: str
    authors: list[str]

# A colleciton of books from open library
class Books(BaseModel):
    data: list[Book]
