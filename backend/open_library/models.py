from pydantic import BaseModel

class Book(BaseModel):
    title: str
    authors: list[str]

class Books(BaseModel):
    data: list[Book]
