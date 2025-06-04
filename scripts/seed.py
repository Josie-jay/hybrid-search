import csv
import random
import numpy as np
from app.database import SessionLocal, init_db
from app.models import MagazineInfo, MagazineContent
from app.utils import get_embedding

def run_seed(csv_file_path: str):
    init_db()
    db = SessionLocal()

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print("Adding info:", row["title"])
            print("Adding content:", row["content"][:50])  # Print first 50 chars
            info = MagazineInfo(
                title=row["title"],
                author=row["author"],
                publication_date=row["publication_date"],
                category=row["category"]
            )
            db.add(info)
            db.flush()  # Get info.id

            content = MagazineContent(
                magazine_id=info.id,
                content=row["content"],
                vector_representation=get_embedding(row["content"])
            )
            db.add(content)

    db.commit()
    db.close()
    print("✅ Database seeded!")

if __name__ == "__main__":
    run_seed("data/sample_data.csv")