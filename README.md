IMPORTANT

In order for project to work, go to *db.py* and in **DB_URL** set up your url to database. Then go to *alembic.ini*, find **sqlalchemy.url** and do the same.

This project presents a simple application which represents a bookstore. It has 3 tables: authors, genres and books.

Table "author" consists of:

1. author_id
2. name_author

Table "genre" consists of:

1. genre_id
2. name_genre - predefined values

Table "book" consists of:

1. book_id
2. title
3. author_id
4. genre_id
5. price - price
6. amount

This project uses **FastAPI**, **Sqlalchemy** and **Alembic** in order to start the local server create migrations from python classes.

If also features the following requests:

1) POST

[
    http://127.0.0.1:8000/authors]() - allows to add author

[
    http://]()[127.0.0.1:8000/authors]() - allows to add a book

2) GET

[
    http://127.0.0.1:8000/authors]() - returns a list of authors

[
    http://127.0.0.1:8000/authors/id]() - returns a selected author by id

[
    http://127.0.0.1:8000/books]() - returns a list of books. Also features queries such as: **f** which allows to search for author by input and **genre** which allows to 		return all books with input genre

[
    http://127.0.0.1:8000/books/id]() - returns a selected book by id

3) DELETE

[
    http://127.0.0.1:8000/authors/id]() - deletes a selected author by id
