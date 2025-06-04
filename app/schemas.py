from pydantic import BaseModel
from typing import List

class SearchRequest(BaseModel):
    query: str
    top_k: int = 10

class SearchResult(BaseModel):
    magazine_id: int
    title: str
    author: str
    score: float

class SearchResponse(BaseModel):
    results: List[SearchResult]