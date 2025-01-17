class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__borrowed = False  # 캡슐화된 속성

    def borrow(self):
        if not self.__borrowed:
            self.__borrowed = True
            return f"You have borrowed '{self.title}'"
        else:
            return f"'{self.title}' is already borrowed"

    def return_book(self):
        if self.__borrowed:
            self.__borrowed = False
            return f"You have returned '{self.title}'"
        else:
            return f"'{self.title}' was not borrowed"
        
    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book}")

    def list_books(self):
        print("Library Collection:")
        for book in self.books:
            print(book)
            
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def __str__(self):
        return f"Library with {len(self.books)} books"

# 객체 생성 및 메소드 호출
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

print(f'1 ===============================')
print(f'book1: {book1}')
print(f'book2: {book2}')

library = Library()

library.add_book(book1)
library.add_book(book2)
library.list_books()
print(f'1 ===============================\n')


class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        return super().__str__() + f" [EBook - {self.file_format}]"
    

class PrintedBook(Book):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.pages = pages

    def __str__(self):
        return super().__str__() + f" [Printed Book - {self.pages} pages]"

# 객체 생성 및 메소드 호출
ebook = EBook("1984", "George Orwell", "1234567890", "PDF")
printed_book = PrintedBook("To Kill a Mockingbird", "Harper Lee", "0987654321", 324)

print(f'2 ===============================')
print(ebook)
print(printed_book)
print()
print(ebook.borrow())
print(ebook.borrow())  # 이미 대출된 도서
print()
print(ebook.return_book())
print(ebook.return_book())  # 이미 반납된 도서
print(f'2 ===============================\n')

# 객체 생성 및 메소드 호출
library = Library()
library.add_book(ebook)
library.add_book(printed_book)
print()

print(f'3 ===============================')
print(library)

found_book = library.find_book_by_title("1984")
if found_book:
    print(f"Found: {found_book}")
else:
    print("Book not found")
print(f'3 ===============================\n')


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        message = book.borrow()
        if "borrowed" in message:
            self.borrowed_books.append(book)
        return message

    def return_book(self, book):
        message = book.return_book()
        if "returned" in message:
            self.borrowed_books.remove(book)
        return message

    def list_borrowed_books(self):
        print(f"{self.name}'s borrowed books:")
        for book in self.borrowed_books:
            print(f'list_borrow: {book}')

# 객체 생성 및 메소드 호출
member = Member("John Doe")

print(f'4 ===============================')

print(f'book2: {member.borrow_book(book2)}')
print(f'ebook: {member.borrow_book(ebook)}')
print(f'ebook: {member.borrow_book(printed_book)}')
print('\n==== nmember.list1 ====')
member.list_borrowed_books()
print()
print(member.return_book(ebook))
print('\n==== nmember.list2 ====')
member.list_borrowed_books()

print(f'4 ===============================')