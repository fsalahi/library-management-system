
from models.book import Book
from services.library import Library
import exceptions, utils

utility = utils.Utils()
myLib = Library("")
myLib.load_books()
utility.menu(myLib)


