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