import logging
from fastapi import FastAPI
#import uvicorn

#from .ml_search.ollama.extract_keywords import extract_keywords

logger = logging.getLogger("uvicorn.error")
logger.warning('loaded app')
app = FastAPI()
@app.get("/api/test")
async def test_ol_fetch():
    logger.warning('Start /api/test')
 #   prompt = "I want books with python in the title"
 #   data = await extract_keywords(prompt)
    data=['test']
    return data

#if __name__ == "__main__":
#    uvicorn.run(app,host="127.0.0.1", port=8000)
