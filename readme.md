# 🧠 Hybrid Search API

This project implements a **hybrid search API** using FastAPI, PostgreSQL with `pgvector`, and OpenAI embeddings. It supports:

- 🔍 **Keyword Search**
- 🧠 **Vector Search**
- ⚡ **Hybrid Search** (keyword + vector)

---

## 🚀 Features
- FastAPI backend
- PostgreSQL + pgvector extension for vector search
- OpenAI API for generating embeddings
- Docker setup for easy environment management

---

## 📁 Project Structure
```
hybrid_search_api/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # SQLAlchemy models
│   ├── database.py          # DB setup & connection
│   ├── schemas.py           # Pydantic schemas
│   ├── search.py            # Search logic
│   └── utils.py             # Helper functions (embeddings)
├── data/
│   └── sample_data.csv      # Sample data
├── scripts/
│   └── seed.py              # DB seeding script
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repo and install dependencies
```bash
git clone https://github.com/Josie-jay/hybrid-search.git
cd hybrid-search
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment
Create a `.env` file:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/magazine_db
OPENAI_API_KEY=your_openai_api_key
```

### 3. Run PostgreSQL with Docker
```bash
docker-compose up -d
```

Make sure `pgvector` extension is enabled:
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### 4. Seed the database
```bash
python -m scripts.seed
```

---

## 🧪 API Usage (via Postman)

### Keyword Search
POST `/search/keyword`
```json
{
  "query": "Fashion",
  "top_k": 5
}
```

### Vector Search
POST `/search/vector`
```json
{
  "query": "outdoor adventures",
  "top_k": 5
}
```

### Hybrid Search
POST `/search`
```json
{
  "query": "pet supplies",
  "top_k": 5
}
```

---

## 🙋‍♀️ Contributing
PRs welcome! Open issues or feature suggestions anytime.

---

## ✨ Author
Built by [@Josie-jay](https://github.com/Josie-jay)
