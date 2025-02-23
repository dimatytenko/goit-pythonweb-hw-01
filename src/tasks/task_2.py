# Завдання 2. SOLID

# Перед вами спрощена програма для керування бібліотекою книг. Програма має можливість додавання нових книг,
# видалення книг та відображення всіх книг у бібліотеці. Користувач має змогу взаємодіяти з програмою через командний рядок,
# використовуючи команди add, remove, show та exit.


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, title, author, year):
#         book = {
#             "title": title,
#             "author": author,
#             "year": year
#         }
#         self.books.append(book)

#     def remove_book(self, title):
#         for book in self.books:
#             if book["title"] == title:
#                 self.books.remove(book)
#                 break

#     def show_books(self):
#         for book in self.books:
#             print(
#                 f'Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}')


# def main():
#     library = Library()

#     while True:
#         command = input(
#             "Enter command (add, remove, show, exit): ").strip().lower()

#         if command == "add":
#             title = input("Enter book title: ").strip()
#             author = input("Enter book author: ").strip()
#             year = input("Enter book year: ").strip()
#             library.add_book(title, author, year)
#         elif command == "remove":
#             title = input("Enter book title to remove: ").strip()
#             library.remove_book(title)
#         elif command == "show":
#             library.show_books()
#         elif command == "exit":
#             break
#         else:
#             print("Invalid command. Please try again.")


# if __name__ == "__main__":
#     main()


# Ваше завдання — переписати код, щоб він відповідав принципам SOLID.


# Ход виконання завдання 2:

# Щоб виконати принцип єдиної відповідальності(SRP), створіть клас Book, який відповідатиме за зберігання інформації про книгу.
# Щоб забезпечити принцип відкритості/закритості(OCP), зробіть так, щоб клас Library міг бути розширений для нової функціональності без зміни його коду.
# Щоб виконати принцип підстанови Лісков(LSP), переконайтеся, що будь-який клас, який наслідує інтерфейс LibraryInterface, може замінити клас Library без порушення роботи програми.
# Щоб виконати принцип розділення інтерфейсів(ISP), використовуйте інтерфейс LibraryInterface для чіткої специфікації методів, які необхідні для роботи з бібліотекою library.
# Щоб виконати принцип інверсії залежностей(DIP), зробіть так, щоб класи вищого рівня, такі як LibraryManager, залежали від абстракцій(інтерфейсів), а не від конкретних реалізацій класів.

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from src.utils.logger_config import logger


@dataclass
class Book:
    title: str
    author: str
    year: str

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        self._books = [book for book in self._books if book.title != title]

    def get_all_books(self) -> List[Book]:
        return self._books.copy()


class BookDisplayInterface(ABC):
    @abstractmethod
    def display_books(self, books: List[Book]) -> None:
        pass


class ConsoleBookDisplay(BookDisplayInterface):
    def display_books(self, books: List[Book]) -> None:
        for book in books:
            logger.info(str(book))


class LibraryManager:
    def __init__(self, library: LibraryInterface, display: BookDisplayInterface):
        self._library = library
        self._display = display

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title=title, author=author, year=year)
        self._library.add_book(book)

    def remove_book(self, title: str) -> None:
        self._library.remove_book(title)

    def show_books(self) -> None:
        books = self._library.get_all_books()
        self._display.display_books(books)


def main():
    library = Library()
    display = ConsoleBookDisplay()
    manager = LibraryManager(library, display)

    while True:
        command = input(
            "Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
