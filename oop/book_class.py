class Book:
    """A class to represent a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor to initialize the book's title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to handle deletion of the Book instance."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation in a user-friendly format."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the Book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' has been created.")

    def __del__(self):
        """Destructor to clean up the Book instance."""
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """String representation of the Book instance."""
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
