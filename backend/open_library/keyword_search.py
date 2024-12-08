import httpx
from .models import Book, Books


async def get_book_suggestions(keywords:list[str]) -> Books:
    #limit to 5, worry about pagination later
    params = { "title": " ".join(keywords),
              "fields": "title,author_name,key",
              "limit": 5 }
    headers = { "User-Agent": "ML OpenLibrary Search (developer@robandjen.com)"}

    async with httpx.AsyncClient() as client:
        response = await client.get("https://openlibrary.org/search.json",
                                     params = params, headers = headers)
        response.raise_for_status()
        # Format of response documented on https://openlibrary.org/dev/docs/api/search
        #         {
        #     "start": 0,
        #     "num_found": 629,
        #     "docs": [
        #         {...},
        #         {...},
        #         ...
        #         {...}]
        # }

        # Each document specified listed in "docs" will be of the following format:

        # {
        #     "cover_i": 258027,
        #     "has_fulltext": true,
        #     "edition_count": 120,
        #     "title": "The Lord of the Rings",
        #     "author_name": [
        #         "J. R. R. Tolkien"
        #     ],
        #     "first_publish_year": 1954,
        #     "key": "OL27448W",
        #     "ia": [
        #         "returnofking00tolk_1",
        #         "lordofrings00tolk_1",
        #         "lordofrings00tolk_0",
        #     ],
        #     "author_key": [
        #         "OL26320A"
        #     ],
        #     "public_scan_b": true
        # }              
        responsedata = response.json()
        docs = responsedata["docs"]
        data: list[Book] = list(map(lambda olbook: Book(title = olbook["title"],
                                                    authors = olbook["author_name"]), docs))
        return Books(data = data)
