
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