
class Book:
    def __init__(
            self,
            title : str,
            author : str,
            year : int,
            available : bool = True
    ) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.available = available


    def borrow(self) -> None:
        self.available = False

    def return_book(self) -> None:
        self.available = True


