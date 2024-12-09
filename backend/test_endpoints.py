
from fastapi import FastAPI
from pydantic import BaseModel

from .ml_search.ollama.extract_keywords import extract_keywords
from .ml_search.ollama.present_books import present_books
from .open_library.keyword_search import get_book_suggestions
from .open_library.models import Books


test_endpoint = FastAPI()

class KeywordList(BaseModel):
    keywords: list[str]

class Prompt(BaseModel):
    prompt: str

class TitleList(BaseModel):
    titles: list[str]

class BookRecommendation(BaseModel):
    recommendation:str

@test_endpoint.post('/keyword_search')
async def do_keyword_search(keywords: KeywordList) -> Books:
    results = await get_book_suggestions(keywords.keywords)
    return results

@test_endpoint.post('/keyword_extract')
async def do_keyword_extract(prompt: Prompt) -> KeywordList:
    results = await extract_keywords(prompt.prompt)
    return results

@test_endpoint.post('/display_suggestions')
async def do_display(titles: TitleList) -> BookRecommendation:
    results = await present_books(titles.titles)
    return BookRecommendation(recommendation=results)
