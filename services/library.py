
import exceptions

class Library:
    def __init__(
            self,
            books
    ):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    
    def show_books(self):
        for book in self.books:
            print(book.title)

    #practice better coding
    def available_books(self):
        return [
                    book.title 
                    for book in self.books
                    if book.available
                ]


    def search_book(self, keyword):
        return[
                book.title
                for book in self.books
                if keyword.lower() in book.title.lower()
        ]

    
    def remove_book(self, bookObj):
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
            print("An unexpected error happened: ", e)
            
    