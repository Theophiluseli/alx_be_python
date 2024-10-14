# Base class for a Book
class Book:
    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for a Book."""
        return f"{self.title} by {self.author}"


# Derived class for an EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook with title, author, and file size."""
        super().__init__(title, author)  # Call the parent class's __init__
        self.file_size = file_size

    def __str__(self):
        """String representation for an EBook."""
        return f"{self.title} by {self.author}, File Size: {self.file_size}MB"


# Derived class for a PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Call the parent class's __init__
        self.page_count = page_count

    def __str__(self):
        """String representation for a PrintBook."""
        return f"{self.title} by {self.author}, Pages: {self.page_count}"


# Library class demonstrating composition
class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f" - {book}")
# Base class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        """Return details of the book (to be overridden by derived classes if needed)."""
        return f"'{self.title}' by {self.author}"

# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class (Book) __init__ method
        self.file_size = file_size

    def get_details(self):
        """Return details specific to an EBook."""
        return f"'{self.title}' by {self.author}, File size: {self.file_size}MB"

# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class (Book) __init__ method
        self.page_count = page_count

    def get_details(self):
        """Return details specific to a PrintBook."""
        return f"'{self.title}' by {self.author}, Pages: {self.page_count}"

# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # List to store Book, EBook, and PrintBook instances

    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all the books in the library with their details."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book.get_details())
