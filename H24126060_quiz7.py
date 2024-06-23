library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    # your code here
    print()
    added = input("Enter the title, genre, and price of the book (separated by |):")
    title, genre, price = added.split("|")
    genre = genre.strip('"') #去除''
    price = float(price)      #改string微浮點數
    library[title] = (genre,price)
    print()
    print(f"Added {title} to the library")
    return True


def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    # your code here
    removed = input("Enter the title of the book to remove:")
    if removed not in library: #如果找不到
        print()
        print(f"Error: {removed} not found in the library.")
        print()
        return False
    else:
        del library[removed] #找到則刪除
        print()
        print(f"Remove {removed} from the library")
        print()
        return True

def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here
    info = input("Enter the title of the book:")
    if info not in library:
        print()
        print(f"Error: {info} not found in the library.")
        print()
    else:
        print()
        print(f"Title: {info}")
        print(f"Genre: {library[info][0]}") #genre
        print(f"Price: {library[info][1]}") #price
        print()

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print()
        print("\nThe library is empty.\n")
        print()
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
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
    found = False
    genre_choosed = input("Enter the genre to search for:")
    print()
    for title, book in sorted(library.items()):
        if book[0] == genre_choosed:
            print(f"{title} {book}")
            found = True #找的到則return True

    if not found:
        print(f"No boooks found in the {genre_choosed} genre")
        print()
        return False
    print()
    return True

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