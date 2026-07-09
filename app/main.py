from fastapi import FastAPI

from app.schemas.book import BookCreate, BookResponse

from app.api.health import router as health_router
from app.config.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


app.include_router(health_router)
@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running",
    }
@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate):
    return {
        "id": 1,
        "title": book.title,
        "author": book.author,
        "year": book.year,
    }

@app.get("/hello")
def hello():
    return {
        "message": "Hello, FastAPI!",
    }

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
    }

@app.get("/search")
def search_items(query: str, limit: int = 10):
    return {
        "query": query,
        "limit": limit,
    }


from pydantic import BaseModel


class ItemCreate(BaseModel):
    title: str
    description: str | None = None
    price: float

@app.post("/items")
def create_item(item: ItemCreate):
    return {
        "message": "Item created",
        "item": item,
    }

from app.api.items import router as items_router

app.include_router(items_router)

from app.database import Base, engine

Base.metadata.create_all(bind=engine)

from fastapi import FastAPI

from app.database import Base, engine
from app.handlers.books import router as books_router
from app.models.book import Book

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(books_router)


@app.get("/")
def root():
    return {"message": "Hello World"}