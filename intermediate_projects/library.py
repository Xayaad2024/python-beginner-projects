# Simple in-memory library system using dictionaries

# Initial library data with available books and members
library = {
    "books": ["Python 101", "AI Basics", "Clean Code"],
    "members": []
}

# Show all available books
def display_books():
    print("\nAvailable Books:")
    for book in library["books"]:
        print(f"- {book}")

# Add a new member to the library
def add_member(name):
    library["members"].append(name)
    print(f"{name} added to members.")

# Borrow a book from the library
def borrow_book(name, book):
    if book in library["books"]:
        print(f"{name} borrowed '{book}'.")
        library["books"].remove(book)  # Remove book from available list
    else:
        print(f"'{book}' is not available.")

# Example usage
display_books()                      # Show books before borrowing
add_member("Ali")                    # Add a new member
borrow_book("Ali", "Python 101")     # Borrow a book
display_books()                      # Show books after borrowing
