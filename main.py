from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import *
from typing import Annotated
from sqlmodel import Session, select
from db import init_db, get_session


app = FastAPI()

@app.get("/authors")
async def get_authors(session: Session = Depends(get_session)) -> list[Author]:
    author_list = session.exec(select(Author)).all()
    
    return author_list


@app.get("/authors/{author_id}")
async def get_author(author_id: Annotated[int, Path(title="The ID of author")], session: Session = Depends(get_session)) -> Author:
    author = session.get(Author, author_id)
    
    return author


@app.post("/authors")
async def add_authors(author_data: AuthorBase, session: Session = Depends(get_session)) -> Author:
    author = Author(name_author=author_data.name_author)

    session.add(author)
    session.commit()
    session.refresh(author)

    return author


@app.get("/books/{book_id}")
async def get_book(book_id: Annotated[int, Path(title="The ID of book")], session: Session = Depends(get_session)):
    book = session.get(Book, book_id)

    return book


@app.get("/books")
async def get_books(f: Annotated[str, Query(max_length=15)] | None = None, 
                    genre: int | None = None,
                    session: Session = Depends(get_session)) -> list[Book]:
    book_list = session.exec(select(Book)).all()

    if f:
        book_list = [b for b in book_list if f.lower() in b.title.lower()]

    if genre:
        book_list = [b for b in book_list if genre == b.genre_id]

    return book_list


@app.post("/books")
async def add_book(book_data: BookBase, session: Session = Depends(get_session)) -> Book:
    book = Book(title=book_data.title, 
                price=book_data.price, 
                amount=book_data.amount, 
                author_id=book_data.author_id,
                genre_id=book_data.genre_id)

    session.add(book)
    session.commit()
    session.refresh(book)

    return book


@app.delete("/authors/{author_id}")
async def delete_author(author_id: Annotated[int, Path(title="The ID of author")], session: Session = Depends(get_session)) -> str:
    author_to_delete = session.exec(select(Author).where(Author.author_id == author_id)).first()

    session.delete(author_to_delete)
    session.commit()

    return f"Author {author_to_delete.name_author} with ID {author_id} was deleted"
