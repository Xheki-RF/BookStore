from datetime import date
from enum import Enum
from pydantic import BaseModel, field_validator
from sqlmodel import SQLModel, Field, Relationship
from fastapi import HTTPException


class GenreChoices(Enum):
    ROMANCE = "romance"
    ADVENTURE = "adventure"
    SCIENCE_FICTION = "science-fiction"
    DETECTIVE = "detective"
    MYSTERY = "mystery"
    FANTASY = "fantasy"
    HISTORICAL = "historical"


class GenreBase(SQLModel):
    name_genre: GenreChoices


class Genre(GenreBase, table=True):
    genre_id: int = Field(default=None, primary_key=True)


class AuthorBase(SQLModel):
    name_author: str

    @field_validator("name_author")
    def capitalize_author(cls, value):
        if len(value.split()) == 3:
            value = value.split()[0] + " " + "".join(value.split()[1:])

        elif len(value.split()) == 1:
            raise HTTPException(status_code=400, detail="Wrong author input. Author template: Ivanov V.V")

        return value.title()


class Author(AuthorBase, table=True):
    author_id: int = Field(default=None, primary_key=True)


class BookBase(SQLModel):
    title: str
    price: float
    amount: int

    author_id: int = Field(foreign_key="author.author_id")
    genre_id: int = Field(foreign_key="genre.genre_id")


class Book(BookBase, table=True):
    book_id: int = Field(default=None, primary_key=True)