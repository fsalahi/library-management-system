
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

    # to save books in a json file, aka dictionary
    def to_dict(self) -> dict:

        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.available
        }
    
    # to convert from json to our Book obj
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            available=data["available"]
        )