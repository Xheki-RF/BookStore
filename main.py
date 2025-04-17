from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import GenreURLChoice, BandBase, BandCreate, Band, Album
from typing import Annotated
from sqlmodel import Session, select
from db import init_db, get_session


app = FastAPI()
