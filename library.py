import time
import sys
class LibraryAccount: #main class
    def __init__(self, user_name, borrowed_books, available_books):
        #setting to instance variables
        self.books = [Book("The Sorcerer's Stone",Author("J.K. Rowling")), Book("The Meltdown",Author("Jeff Kinney")), Book("Moon Rising",Author("Tui T. Sutherland")), Book("The Secret Garden",Author("Frances Hodgson Burnett")), Book("Call of The Wild",Author("Jack London")), Book("The Desert Quest",Author("Ayad Haider"))] 
        self.borrowed_books = borrowed_books
        borrowed_books = [""] #default is empty
        self.available_books = available_books
        available_books = ["The Sorcerer's Stone", "The Meltdown", "Moon Rising", "The Secret Garden", "Call of The Wild", "The Desert Quest"]
    def show_available_books(self):
        print(f"The available books are {self.available_books}")
    def borrow_book(self, book_title):
        self.book_title = book_title
        book_title = input("Type the book you want:")
        if book_title in available_books:
            borrowed_books.append(book_title)
            available_books.remove(book_title)
            print("The book has been borrowed.")
        else:
            print("The book was already borrowed or does not exist.")
    def return_book(self, book_title):
        book_title = input("Which book do you want to return?:")
        if book_title in borrowed_books:
            borrowed_books.remove(book_title)
            available_books.append(book_title)
            print(f"The book {book_title} has been returned.")
        else:
            print("The book was never borrowed.")
class Author:
    def __init__(self, name):
        self.name = name
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        pass

AccountSession = LibraryAccount("Alice","",["The Sorcerer's Stone", "The Meltdown", "Moon Rising", "The Secret Garden", "Call of The Wild", "The Desert Quest"])

print("Library Menu:\n 1. Show Available Books \n 2. Borrow a Book \n 3. Return a Book \n 4. Exit")
choice = input("Choose your option: ")
if choice == "1":
    AccountSession.show_available_books()
    time.sleep(1)
if choice == "2":
    AccountSession.borrow_books()
if choice == "3":
    AccountSession.return_book()
if choice == "4":
    print("Goodbye!")
    sys.exit()
