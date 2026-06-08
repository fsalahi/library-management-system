
class Book:
    def __init__(
            self,
            title,
            author,
            year,
            available = True
    ):
        self.title = title
        self.author = author
        self.year = year
        self.available = available


    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True


