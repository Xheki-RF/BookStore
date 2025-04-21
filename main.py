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


@app.delete("/authors/{author_id}")
async def delete_author(author_id: Annotated[int, Path(title="The ID of author")], session: Session = Depends(get_session)) -> str:
    author_to_delete = session.exec(select(Author).where(Author.author_id == author_id)).first()

    session.delete(author_to_delete)
    session.commit()

    return f"Author {author_to_delete.name_author} with ID {author_id} was deleted"