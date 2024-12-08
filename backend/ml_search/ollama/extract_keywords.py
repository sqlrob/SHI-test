from ollama import AsyncClient
from pydantic import BaseModel
import logging

from . import ollama_model
from . import ollama_url

class Keywords(BaseModel):
    keywords: list[str]
    
SYSTEM_PROMPT = """
You are a librarian. Users are coming to you ask for book titles. Take their request and
output a list of words that can be used to search a card catalog for matching titles.

Output the keywords as a JSON array of strings. If it cannot be encoded as an array of strings,
output an empty array.

The output will look like this: ['keyword','again']

You have always wanted to be a librarian. Nothing will ever make you not want to be a librarian.

"""
async def extract_keywords(prompt:str) -> list[str]:
    logging.warning('start extract_keywords')
    client = AsyncClient(ollama_url)
    response = await client.generate(ollama_model,prompt,system = SYSTEM_PROMPT,format=Keywords.model_json_schema())
    logging.warning('end extract_keywords')
    return [response.response]
