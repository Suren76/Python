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

    def __init__(self, first_name, last_name, gender, age, id, reads_book, favorite_books, books_to_read_later):
        super().__init__(first_name, last_name, gender, age)
        self.id = id
        self.reads_book = reads_book
        self.favorite_books = favorite_books
        self.books_to_read_later = books_to_read_later

    def __str__(self):
        return f"{self.full_name}  {self.gender}  {self.age}  {self.id}  {self.reads_book}  {self.favorite_books} " \
               f" {self.books_to_read_later}"


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

    def __str__(self):
        return f"{self.__title}  {str(self.__author)}  {self.__published_date}"


class Library:

    def __init__(self, address, books, readers):
        self.address = address
        self.books = books
        self.readers = readers

    @property
    def books_quantity(self):
        return len(self.books)

    def add_book(self, new_book):
        self.books.append(new_book)

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

    def __str__(self):
        return f"{self.address}  {self.books_quantity}  {len(self.readers)}"
