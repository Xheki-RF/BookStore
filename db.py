from sqlmodel import create_engine, SQLModel, Session

DB_URL = "postgresql://postgres:Pc4423342@127.0.0.1:5432/book_store"

engine = create_engine(DB_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
