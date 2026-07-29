
from models.book import Book
from services.library import Library
import utils

utility = utils.Utils()
myLib = Library("")
myLib.load_books()
#myLib.save_books()

utility.menu(myLib)

myLib.show_books()

# Remove book from library
# myLib.remove_book(myLib.choose_one_book("let me go"))
# myLib.show_books()




