# book_class.py

class book:
    def __inti__(self, title: str, author:str, year: int):
         """Constructor that initializes a Book instance with title, author, and year."""
         self.title = title
         self.author = author
         self.year = year
         print(f"book created: {self.title} by {self.author}, published in {self.year}")
    def __del__(self):
         """Destructor that prints a message when a Book instance is deleted."""
         print(f"deleting book: {self.title} by {self.author}")
    def __str__(self):
         """User-friendly string representation of the Book."""
         return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
            """Official string representation of the Book."""
            return f"Book('{se;f.title}', '{self.author}', published in {self.year})"

# example usage (for testing purposes):
if __name__ == "__main__":
     book1 = Book("1984", "George Orwell", 1949)
     print(str(book1)) #uses __str__
     print(repr(book1)) #uses __repr__
     del book1
         
              