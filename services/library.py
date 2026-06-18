
import exceptions
from models.book import Book
import json

class Library:
    def __init__(
            self,
            books
    ) -> None:
        self.books : list[Book] = []

    def add_book(self, book : Book) -> None:
        self.books.append(book)

    
    def show_books(self) -> None:
        for book in self.books:
            print(book.title)



    #practice better coding
    def available_books(self) -> list[str]:
        return [
                book.title 
                for book in self.books
                if book.available
            ]


    def search_book(self, keyword : str) -> list[str]:
        return[
                book
                for book in self.books
                if keyword.lower() in book.title.lower()
        ]

    
    def remove_book(self, bookObj : Book) -> None:
        try:
            for book in self.books:
                if book.title == bookObj.title and book.author == bookObj.author:
                    print("Success! The book ", bookObj.title, " was removed.")
                    self.books.remove(book)
                    return
            
            raise exceptions.BookNotFoundError(f"'{bookObj.title}' not found.")
        
        except exceptions.BookNotFoundError:
            print("Error: The book [", bookObj.title, "] does not exist!")
        
        except Exception as e:
            print("An unexpected error happened in remove_book() function: ", e)
            
    
    def save_books(self) -> None:
        try:
            books_data = [
                book.to_dict()
                for book in self.books
            ]
            with open(
                "data/books.json",
                "w" #overwrite if exists, create otherwise.
            ) as file:
                json.dump(
                books_data,
                file,
                indent=4 # readabality purposes: adding a newline and 4 spaces for each level of nesting
            )
        except Exception as e:
            print("An unexpected error happened in save_books() function: ", e)

            
    def load_books(self) -> None:
        try:
            with open(
                "data/books.json",
                "r"
            ) as file:

                data = json.load(file)
            
            for book_data in data:
                book = Book.from_dict(book_data)
                self.books.append(book)
        except Exception as e:
            print("An unexpected error happened in load_books() function: ", e)

    def choose_one_book(self, keyword : str) -> Book:
        searched_book = self.search_book(keyword)
        searched_book_len = len(searched_book)
        if searched_book_len > 1:
            print("There are multiple books with this search, please be more specific.")
            for book in searched_book:
                print(book.title)
            return None
        elif searched_book_len == 1:
            return searched_book[0]
        elif searched_book_len == 0:
            print("Sorry! Our library doesn't have this book.")
            return None