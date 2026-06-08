
from models.book import Book
from services.library import Library

# test
book1 = Book(
    "A Story",
    "Fatima Salahi",
    2022
)
book2 = Book(
    "Another Story",
    "Fatima Salahi",
    2023
)
myLib = Library("")
myLib.add_book(book1)
myLib.add_book(book2)

myLib.show_books()
print("All available books: ", myLib.available_books())
print(myLib.search_book("st22ory"))