class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = True
    def borrow(self):
        if self.__available:
            self.__available = False
        else:
            print(f"Książka '{self.__title}' jest już wypożyczona.")
    def return_book(self):
        self.__available = True
    def is_available(self):
        return self.__available
    def get_info(self):
        return f"Tytuł: {self.__title}, Autor: {self.__author}, ISBN: {self.__isbn}, Dostępność: {'Tak' if self.__available else 'Nie'}"

class Person:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number
    def get_info(self):
        return f"Imię i nazwisko: {self.__name}, Numer ID: {self.__id_number}"
class Reader(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self.borrowed_books = []
    def borrow_book(self, book: Book):
        if book.is_available():
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.get_info()} wypożyczył(a) książkę: '{book.get_info()}'.")
        else:
            print(f"Książka '{book.get_info()}' jest niedostępna.")
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.get_info()} zwrócił(a) książkę: '{book.get_info()}'.")
        else:
            print(f"Książka '{book.get_info()}' nie została wypożyczona przez tego czytelnika.")

class Librarian(Person):
    def check_availability(self, book: Book):
        print(f"Książka '{book.get_info()}' jest {'dostępna' if book.is_available() else 'niedostępna'}.")
    def register_book(self, title, author, isbn):
        print(f"Zarejestrowano nową książkę: Tytuł: {title}, Autor: {author}, ISBN: {isbn}")
        return Book(title, author, isbn)

librarian = Librarian("Agata Milewska", "BCB001")
reader = Reader("Anna Nowak", "READ001")
book1 = librarian.register_book("Hobbit", "J.R.R. Tolkien", "123456789")
book2 = librarian.register_book("Harry Potter", "J.K. Rowling", "987654321")
librarian.check_availability(book1)
librarian.check_availability(book2)
reader.borrow_book(book1)
reader.borrow_book(book2)
reader.borrow_book(book1)
librarian.check_availability(book1)
reader.return_book(book1)
librarian.check_availability(book1)
