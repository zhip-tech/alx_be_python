class Book:
    """Represents a book with a title, author, and availability state."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False   # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out



class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book '{title}' not found in library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in library.")

    def list_available_books(self):
        """Print all books that are available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
