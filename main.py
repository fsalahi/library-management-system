
from models.book import Book
from services.library import Library

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
        print("The book is added to the library.")

    elif choice == "2":
        myLib.show_books()

    elif choice == "3":
        print("Borrow book: ")
        title = input("Title: ")
        selected_book = myLib.choose_one_book(title)
        if selected_book and selected_book.available:
            selected_book.borrow()
            print("You borrowed the book: ", selected_book.title, " for 2 weeks!")
        elif selected_book and not selected_book.available:
            print("Currently this book is not available to borrow!")

    elif choice == "4":
        print("Return book: ")
        title = input("Title: ")
        selected_book = myLib.choose_one_book(title)
        if selected_book:
            selected_book.return_book()
            print("You returned the book [", selected_book.title, "]. Thanks!")

    elif choice == "5":
        title = input("What is the title you are looking for? ")
        matching_books = myLib.search_book(title)
        if len(matching_books) >= 1:
            print("Here are the books with your search:")
            for book in matching_books:
                print(
                    f"Title: {book.title} \t| "
                    f"Author: {book.author} \t| "
                    f"Available: {book.available}")
        else:
            print("There was no result for this search!")

    elif choice == "6":
        myLib.save_books()
        print("Books are saved!")

    elif choice == "7":
        myLib.save_books()
        print("Goodbye!")
        break

    else:
        print("Error")