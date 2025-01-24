class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation for a user-friendly description of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation to recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
