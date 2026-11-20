from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "author": "Ali",
        "available": True,
    },
    {
        "id": 2,
        "title": "Backend Development",
        "author": "Nigar",
        "available": True,
    },
    {
        "id": 3,
        "title": "Web Programming",
        "author": "Murad",
        "available": False,
    },
]


@app.get("/")
def root():
    return {"message": "Welcome to the Library API!"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Library API is running",
    }


@app.get("/books")
def get_books():
    return {
        "books": books,
        "total": len(books),
    }


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found",
    )


@app.get("/about")
def about():
    return {
        "project": "Library API",
        "version": "1.0.0",
        "book_count": len(books),
    }
