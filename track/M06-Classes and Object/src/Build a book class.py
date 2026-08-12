class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

title = input().strip() 
author = input().strip()
price = int(input())

book = Book(title, author, price)
print("BOOK DETAILS")
print(f"Book Title: {book.title}")
print(f"Author: {book.author}")
print(f"Price: {book.price}")

#define a class book with __init__ method that accepts title, author, and price
#read the values from user input and create an instance of the book class
#print all details of the book in the specified format