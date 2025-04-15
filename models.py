from datetime import date
from enum import Enum
from pydantic import BaseModel, field_validator
from sqlmodel import SQLModel, Field, Relationship


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


class Author(AuthorBase, table=True):
    author_id: int = Field(default=None, primary_key=True)