from fastapi import FastAPI
from data_processing import library_data, Book

app = FastAPI()

library = library_data("library.json")
books = library.books


@app.get("/books")
async def read_books():
    return books

# path parameter
@app.get("/books/title/{title}")
async def read_book_by_title(title: str):
    return [book for book in books if book.title.casefold() == title.casefold()]


@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)
    books.append(new_book)

    return new_book

@app.get("/books/genres/{genre}")
async def read_books_by_genre(genre: str):
    return [book for book in books if genre in book.genres]

# TODO: 
# update
# delete
# query parameters

#add genre


# @app.put("/books")

# Ni söker rollen Machine learning engineer

#Ni får detta som arbetsprov:

#Använd er av det vi gick igenom igår om FastAPI CRUD

#bygg vidare på det
#lär er innehållet
#kommunicera tekniskt
#presentera det (kan kombinera egna slides med kod) - ca 5 min presentation - sen kommer frågor och diskussioner
#hur kan man bygga ut det
#kan man bygga liknande med annan data än books?
 
