# Notes of library system project

## Review:
- self in classes: represents the specific instance of the class that is currently being built or called. In python, objects are explicitly passed as the first argument of the class.
- __init__: automatic setup to configure data the moment we instantiate a class
- Simply put, we need __init__ to set up object's data, and self to remember that data later.


## Better coding practices
- look at function available_books() in library.py
    expression
    for item
    in iterable
    if condition

- look at return statement in search_book in Library.py
    this lists all matching books. what if you want to stop the scan once you found the first match? then use next(). something like this: return next(
    (book.title for book in self.books if keyword.lower() in book.title.lower()), None)

- Use type hints: they explicitly declare what data types variables, function arguments, and return values should be, but do not enforce types at runtime.

- Even though this is just a practice/small project, let's have data stored somewhere (like JSON, APIs usually return json) instead of RAM.

- In save_books() function in Library.py I used with open(...) instead of file = open(...) because I need to remember to close when I open file by former way. with open(...) closes the file automatically.


## Steps I take when initializing a project
    - create folder and files structure
    - inside: git init
    - create .gitignore file and inside I list things that I want to exclude from pushing to github
    - create virtual env and activate it
    - install needed packages and save them (freeze) in requirements.txt
    - make your first commit
    - make repository in github
    connect local git to github (git remote add origin [url to repository])
    - git push -u origin main

