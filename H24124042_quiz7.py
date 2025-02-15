library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """
    # your code here
    book_info= input("Enter the book title, genre, and price (separated by '|'): ")
    book_info=book_info.split("|")
    title=book_info[0]
    genre=book_info[1]
    price=book_info[2]
    if title in library:
        print("{} already exists in the library.".format(title))
    else:
        library[title] = {"genre": genre, "price": price}
        print("{} has been added to the library.".format(title))
    print("Current library books:")
    if len(library) == 0:
        print("No books in the library.")
    else:
        for title in sorted(library.keys()):
           # print(f"{title} ({library[title]['genre']}, {library[title]['price']})")
            print(title, "({}, ${})".format(library[title]["genre"],library[title]["price"]))

def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    # your code here
    title = input("Enter the title of the book you want to remove: ")
    if title in library:
        del library[title]
        print("{} has been removed from the library.".format(title))
    else:
        print("Error: {} is not in the library.".format(title))
def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here
    title = input("Enter the title of the book: ")
    if title in library:
        print("Title: {}\nGenre: {}\nPrice: {}".format(title,library[title]["genre"],library[title]["price"]))
    else:
        print("Error: {} is not in the library.".format(title))

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("{} ({}, {})".format (title, library[title]["genre"], library[title]["price"]))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here
    genre = input("Enter the genre to search for: ")
    books_found = False
    for title, book_info in sorted(library.items()):
        if book_info["genre"] == genre:
            if not books_found:
                print("All books in the {} genre:".format("genre"))
                books_found = True
            print("{} ({}, ${})".format(title,book_info['genre'],book_info['price']))
    if not books_found:
        print(f"No books found in the {genre} genre.")

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

