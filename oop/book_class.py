class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Called when the object is about to be destroyed
        print(f"Deleting {self.title}")

    def __str__(self):
        # Human-friendly representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official representation that can recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
