import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .ml_search.ollama.present_books import present_books
from .open_library.keyword_search import get_book_suggestions

from .ml_search.ollama.extract_keywords import extract_keywords
from .test_endpoints import test_endpoint

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins = ["http://localhost:3000"],
                   allow_methods = ["*"],
                   allow_headers=["*"])

class RecommendationRequest(BaseModel):
    request:str

class RecommendationResponse(BaseModel):
    response:str

logger = logging.getLogger('uvicorn.error')

@app.post("/api/recommend")
async def get_book_recommendation(request:RecommendationRequest) -> RecommendationResponse:
    keywords = await extract_keywords(request.request)
    search_results = await get_book_suggestions(keywords.keywords)
    logger.warning("search_results='%s', type='%s'",search_results, type(search_results))
    title_list = list(map(lambda x: x.title, search_results.data))
    full_recommendation = await present_books(title_list)
    return RecommendationResponse(response=full_recommendation)


app.mount('/test', test_endpoint)
