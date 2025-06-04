from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import SearchRequest, SearchResponse
from app.search import hybrid_search, keyword_search, vector_search
from app.utils import get_embedding

app = FastAPI()


@app.post("/search/keyword", response_model=SearchResponse)
def search_keyword(request: SearchRequest, db: Session = Depends(get_db)):
    keyword_results = keyword_search(request.query, db, top_k=request.top_k)
    results = [{
        "magazine_id": item.id,
        "title": item.title,
        "author": item.author,
        "score": 1.0
    } for item in keyword_results]
    return {"results": results}


@app.post("/search/vector", response_model=SearchResponse)
def search_vector(request: SearchRequest, db: Session = Depends(get_db)):
    embedding = get_embedding(request.query)
    vector_results = vector_search(embedding, db, top_k=request.top_k)
    results = [{
        "magazine_id": vc.magazine.id,
        "title": vc.magazine.title,
        "author": vc.magazine.author,
        "score": 0.9
    } for vc in vector_results]
    return {"results": results}

@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest, db: Session = Depends(get_db)):
    embedding = get_embedding(request.query)
    results = hybrid_search(request.query, embedding, db, top_k=request.top_k)
    return {"results": results}