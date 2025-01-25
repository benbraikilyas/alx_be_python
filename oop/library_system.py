class Book:
    """Base class for all types of books."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class EBook(Book):
    """Class representing an electronic book."""
    
    def __init__(self, title, author, file_size):
        """Initialize an ebook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size  # in KB
    
    def __str__(self):
        """Return a string representation of the ebook."""
        return f"{super().__str__()} [{self.file_size}KB]"


class PrintBook(Book):
    """Class representing a physical printed book."""
    
    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return a string representation of the print book."""
        return f"{super().__str__()} ({self.page_count} pages)"


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
        if not self.books:
            print("The library is empty.")
            return
        
        print("\nLibrary Catalog:")
        print("-" * 50)
        
        # Group books by type
        regular_books = [book for book in self.books if type(book) is Book]
        ebooks = [book for book in self.books if isinstance(book, EBook)]
        print_books = [book for book in self.books if isinstance(book, PrintBook)]
        
        if regular_books:
            print("\nRegular Books:")
            for book in regular_books:
                print(f"  • {book}")
        
        if ebooks:
            print("\nE-Books:")
            for book in ebooks:
                print(f"  • {book}")
        
        if print_books:
            print("\nPrint Books:")
            for book in print_books:
                print(f"  • {book}")
        
        print(f"\nTotal Books: {len(self.books)}")






from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook(""Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
