class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)


book = Book("The Fellowship of the Ring", "JRR Tolkien")

print(book)
print(len(book))