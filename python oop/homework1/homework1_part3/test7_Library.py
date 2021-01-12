# line 127  bookId -> book_id, expirationDate -> expiration_date
# line 58 readerId -> reader_id
# line 162 do_have_book -> check_book
# line 153 add_book,add_books -> add_book

class Person:

    def __init__(self, first_name, last_name, gender, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.age = age

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def gender(self):
        return self.__gender

    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name

    def __str__(self):
        return f"{self.full_name}  {self.__gender}  {self.age}"


class Author(Person):

    def __init__(self, first_name, last_name, gender, age, email, pseudonym=None):
        super().__init__(first_name, last_name, gender, age)
        self.email = email
        self.pseudonym = pseudonym

    def __str__(self):
        if self.pseudonym is None:
            return f"{self.full_name}  {self.gender}  {self.age}  {self.email}"
        else:
            return f"{self.full_name}  {self.gender}  {self.age}  {self.email}  {self.pseudonym}"


class Reader(Person):

    def __init__(self, first_name, last_name, gender, age, reader_id, reads_book, favorite_books, books_to_read_later):
        super().__init__(first_name, last_name, gender, age)
        self.reader_id = reader_id
        self.reads_book = reads_book
        self.favorite_books = favorite_books
        self.books_to_read_later = books_to_read_later

    def borrow_book(self, book, library):
        if library.check_book(book.title, book.author) is True and type(book) == ReaderBook:
            self.books_to_read_later.append(book)

    def __str__(self):
        return f"{self.full_name}  {self.gender}  {self.age}  {self.reader_id}  {self.reads_book}   \
               {self.favorite_books} {self.books_to_read_later}"


class Book:

    def __init__(self, title, author, published_date):
        self.__title = title
        self.__author = author
        self.__published_date = published_date

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return str(self.__author)

    @property
    def published_date(self):
        return self.__published_date

    @property
    def author_name(self):
        if self.__author.pseudonym is None:
            return self.__author.full_name
        else:
            return self.__author.pseudonym

    def is_the_same_book(self, book):
        if self.__author == book.author and self.__title == book.title:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.__title}  {str(self.__author)}  {self.__published_date}"


class LibraryBookBase(Book):

    def __init__(self, book_id, title, author, published_date):
        super().__init__(title, author, published_date)
        self.book_id = book_id

    def __str__(self):
        return f"{self.book_id}: {self.title}  {str(self.author)}  {self.published_date}"


class LibraryBook(Book):
    def __init__(self, book_id, title, author, published_date, quantity):
        super().__init__(title, author, published_date)
        self.book_id = book_id
        self.quantity = quantity

    def increase_quantity_by(self, amount):
        self.quantity += amount

    def decrease_quantity_by(self, amount):
        self.quantity -= amount

    def __str__(self):
        return f"{self.title}  {str(self.author)}  {self.published_date}  {self.book_id}  {self.quantity}"


class ReaderBook(Book):
    def __init__(self, book_id, expiration_date, is_returned, title, author, published_date):
        super().__init__(title, author, published_date)
        self.book_id = book_id
        self.expiration_date = expiration_date
        self.is_returned = is_returned

    def __str__(self):
        return f"{self.title}  {str(self.author)}  {self.published_date}  {self.book_id}  {self.expiration_date} \
                 {self.is_returned}"


class Library:

    def __init__(self, address, books, readers):
        self.address = address
        self.books = books
        self.readers = readers

    @property
    def books_quantity(self):
        return len(self.books)

    def add_book(self, new_book):
        def check_new_book(check_book):
            if self.check_book(check_book.title, check_book.author) is False:
                self.books.append(check_book)
            else:
                i = 0
                for book in self.books:
                    if book.title == check_book.title and book.author == check_book.author:
                        self.books[i].increase_quantity_by(1)
                    i += 1

        if len(new_book) == 1:
            check_new_book(new_book)

        if len(new_book) > 1:
            for _ in new_book:
                check_new_book(_)

        return self.books

    def check_reader(self, reader_id):
        for reader in self.readers:
            if reader_id == reader.id:
                return True
        return False

    def check_book(self, book_title, book_author):
        for book in self.books:
            if book.title == book_title and book.author == book_author:
                return True
        return False

    def lend_book(self, book, reade_id):
        if self.check_book(book.title, book.author) is True and self.check_reader(reade_id) is True and \
                type(book) == ReaderBook:
            return book

    def __str__(self):
        return f"{self.address}  {self.books_quantity}  {len(self.readers)}"
