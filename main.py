
from models.book import Book
from services.library import Library

# # initialize test
# book1 = Book(
#     "A Story",
#     "Fatima Salahi",
#     2022
# )
# book2 = Book(
#     "Another Story",
#     "Fatima Salahi",
#     2023
# )
# # do not add book3 to the library
# book3 = Book(
#     "goast book",
#     "no author",
#     2023
# )
# myLib = Library("")
# myLib.add_book(book1)
# myLib.add_book(book2)

# myLib.show_books()
# print("All available books: ", myLib.available_books())
# print(myLib.search_book("st22ory"))

# test remove
# myLib.remove_book(book2)
# myLib.show_books()
# print("All available books: ", myLib.available_books())

#myLib.save_books() # after running this once I commented the code above
myLib = Library("")
myLib.load_books() # because this will load the books from json file
# myLib.show_books()

# today let's create a simple menu for users
while True:

    print("\nLibrary Menu")

    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Save Books")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Add book: ")
        title = input("Title: ")
        author = input("Author: ")
        year = int(input("Year: "))
        book = Book(title, author, year, True)
        myLib.add_book(book)
    elif choice == "2":
        myLib.show_books()
    elif choice == "3":
        print("Borrow book: ")
        title = input("Title: ")
        searched_book = myLib.search_book(title)
        if len(searched_book) > 1:
            print("Here are the books with your search, please be more specific.")
            for book in searched_book:
                print(book.title)
        elif len(searched_book) == 1 and searched_book[0].available:
            searched_book[0].borrow()
            print("You borrowed the book: ", searched_book[0].title, " for 2 weeks!")
        elif len(searched_book) == 1 and not searched_book[0].available:
            print("This book is not available at the moment.")
        elif len(searched_book) == 0:
            print("Sorry! Our library doesn't have this book.")  
    elif choice == "7":
        myLib.save_books()
        print("Hope to see you soon!")
        break
    else:
        print("Error")