class Account:

    def __init__(self, id, first_name, last_name, balance):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance

    @property
    def id(self):
        return self.__id

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
    def balance(self):
        return self.__balance

    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def credit(self, amount):
        self.__balance += amount
        return self.__balance

    def debit(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Amount exceeded balance."

    def transfer_to(self, another_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            another_account.balance += amount
            return self.__balance
        else:
            return "Amount exceeded balance."

    @staticmethod
    def identify_accounts(account_first, account_second):
        if account_first.full_name == account_second.full_name or account_first.id == account_second.id:
            return "Account is dublicated"
        else:
            return "Account is not dublicated"

    def __str__(self):
        return f"{self.__id}  {self.full_name}  {self.__balance}"


Suren = Account(1, "Suren", "Parsyan", 11200)
Gor = Account(2, "Gor", "Parsyan", 113400)
print(Suren.debit(1000))
print(Suren.transfer_to(Gor, 100), Gor.balance)
print(Suren.identify_accounts(Suren, Gor))
print(str(Suren))
