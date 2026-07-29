
import exceptions
from models.book import Book
import json

class Library:
    def __init__(
            self,
            books
    ) -> None:
        #self.books : list[Book] = []
        self.books : dict = {} # key: book.tilte, value: book


    def load_books(self) -> None:
        try:
            with open("data/books.json", "r") as file:
                # 1. Load the data (this will be a list of dicts)
                loaded_list = json.load(file)
                # 2. Reset self.books to an empty dictionary
                self.books = {}
                
                # 3. Populate dictionary using the title as the key
                for book_data in loaded_list.values():
                    title = book_data.get("title")
                    if title:
                        self.books[title] = book_data
                    else:
                        print("Warning: Found a book with a missing title field!")
                        
        except FileNotFoundError:
            print("Error: The file data/books.json was not found.")
        except Exception as e:
            print("An unexpected error happened in load_books() function: ", e)



    def add_book(self, book : Book) -> None:
        self.books[book.title] = book.to_dict()

    
    def show_books(self) -> None:
        # for book in self.books:
        #     print(book.title)
        for key in self.books:
            print(key)



    def available_books(self) -> dict:
        return {
                book["title"] : book
                for book in self.books.values()
                if book["available"]
        }


    def search_book(self, keyword: str) -> list[Book]:
        return [
            Book(**book)  #creates a Book instance from the dictionary
            for book in self.books.values()
            if keyword.lower() in book["title"].lower()
        ]

    
    def remove_book(self, bookObj : Book) -> None:
        try:
            for book in self.books.values():
                if book["title"] == bookObj.title and book["author"] == bookObj.author:
                    del self.books[bookObj.title] #self.books.pop(book["title"])
                    print("Success! The book [", bookObj.title, "] was removed.")
                    self.save_books()
                    return
            
            raise exceptions.BookNotFoundError(f"'{bookObj.title}' not found.")
        
        except exceptions.BookNotFoundError:
            print("Error: The book [", bookObj.title, "] does not exist!")
        
        except Exception as e:
            print("An unexpected error happened in remove_book() function: ", e)
            
    
    def save_books(self) -> None:
        try:
            with open(
                "data/books.json",
                "w" #overwrite if exists, create otherwise.
            ) as file:
                json.dump(
                self.books,
                file,
                indent=4 # readabality purposes: adding a newline and 4 spaces for each level of nesting
            )
        except Exception as e:
            print("An unexpected error happened in save_books() function: ", e)


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