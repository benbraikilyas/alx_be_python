class Book:
    """Base class for all types of books."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Class representing an electronic book."""
    
    def __init__(self, title, author, file_size):
        """Initialize an ebook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size  # in KB
    
    def __str__(self):
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by Neal Stephenson, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Class representing a physical printed book."""
    
    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that can hold different types of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            return True
        return False
    
    def list_books(self):
        """Display all books in the library."""
        for book in self.books:
            print(book)  # Directly print each book's string representation
        print(f"\nTotal Books: {len(self.books)}")  # Add total books count


from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
