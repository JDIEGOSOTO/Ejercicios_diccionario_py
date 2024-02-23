class Biblioteca():
    def __init__(self):
        self.books = {}

    def add_book(self): 
        libro_id = str(len(self.books) + 1)
        title = input("Type the name of the book you want to add: ")
        author = input("Type the autor of the book: ")
        year = int(input("Type the year of the book: "))
        self.books[libro_id] = { "title" : title, "author" : author, "year" : year}
        print("Book added!")

    def show_books(self):
        print("List of books: ")
        for id, book in self.books.items():
            print(f"Book {id}: ")
            book_info =f"Title: {book["title"].title()}, Author: {book["author"].title()}, Year: {str(book["year"])}"
            print(book_info)

library1 = Biblioteca()
library1.add_book()
library1.add_book()
library1.show_books()
