class Author:

    def __init__(self, first_name, last_name, email, gender):
        self.__first_name = first_name
        self.__last_name = last_name
        self.email = email
        self.__gender = gender

    @property
    def last_name(self):
        return self.__last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def gender(self):
        return self.__gender

    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def __str__(self):
        return f"{self.__first_name, self.__last_name} {self.email} {self.__gender}"


class Book:

    def __init__(self, title, author, release_date, price, quantity):
        self.__title = title
        self.__author = author.full_name()
        self.__release_date = release_date
        self.price = price
        self.quantity = quantity

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def release_gate(self):
        return self.__release_date

    def profit(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.__title}, {self.__author}, {self.__release_date}, {self.price}, {self.quantity}"


book_author = Author("Suren", "Parsyan", "hhkjh@mail.ru", "male")
book = Book("book_name", book_author, 1992, 466, 5555)
print(str(book))
