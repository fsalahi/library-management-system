
from models.book import Book
from services.library import Library

# initialize test
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
# do not add book3 to the library
book3 = Book(
    "goast book",
    "no author",
    2023
)
myLib = Library("")
myLib.add_book(book1)
myLib.add_book(book2)

myLib.show_books()
print("All available books: ", myLib.available_books())
print(myLib.search_book("st22ory"))

#test remove
myLib.remove_book(book2)
myLib.show_books()
print("All available books: ", myLib.available_books())