from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import MagazineInfo, MagazineContent
from typing import List, Dict

def keyword_search(query: str, db: Session, top_k: int = 10):
    return db.query(MagazineInfo).join(MagazineContent).filter(
        or_(
            MagazineInfo.title.ilike(f"%{query}%"),
            MagazineInfo.author.ilike(f"%{query}%"),
            MagazineContent.content.ilike(f"%{query}%")
        )
    ).limit(top_k).all()

def vector_search(embedding: List[float], db: Session, top_k: int = 10):
    return db.query(MagazineContent).order_by(
        MagazineContent.vector_representation.l2_distance(embedding)
    ).limit(top_k).all()

def hybrid_search(query: str, embedding: List[float], db: Session, top_k: int = 10) -> List[Dict]:
    keyword_matches = keyword_search(query, db, top_k)

    vector_matches = vector_search(embedding, db, top_k)

    results = []
    seen = set()

    # Combine with simple score heuristic
    for item in keyword_matches:
        results.append({
            "magazine_id": item.id,
            "title": item.title,
            "author": item.author,
            "score": 1.0
        })
        seen.add(item.id)

    for vc in vector_matches:
        if vc.magazine_id not in seen:
            results.append({
                "magazine_id": vc.magazine.id,
                "title": vc.magazine.title,
                "author": vc.magazine.author,
                "score": 0.9
            })

    return sorted(results, key=lambda x: -x["score"])[:top_k]