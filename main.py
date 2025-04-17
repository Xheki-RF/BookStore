from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import *
from typing import Annotated
from sqlmodel import Session, select
from db import init_db, get_session


app = FastAPI()

@app.post("/authors")
async def add_authors(author_data: AuthorBase, session: Session = Depends(get_session)) -> Author:
    author = Author(name_author=author_data.name_author)

    session.add(author)
    session.commit()
    session.refresh(author)

    return author