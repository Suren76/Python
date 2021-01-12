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


class Student(Person):

    def __init__(self, first_name, last_name, gender, age, programs, year, fee):
        super().__init__(first_name, last_name, gender, age)
        self.programs = programs
        self.year = year
        self.fee = fee

    def pass_exam(self):
        exam_res = {}
        for val in self.programs:
            if val["grade"] >= 50:
                exam_res[str(val)] = "Pass"
            else:
                exam_res[str(val)] = "Fail"

        self.__exam_res = exam_res

        if set(exam_res.values()) == {"Pass"}:
            self.year += 1

        return self.year

    @property
    def exam_result(self):
        return self.__exam_res

    def __str__(self):
        return f"{self.full_name}  {self.gender}  {self.age}  {self.programs}  {self.year}  {self.fee}"


class Teacher(Person):
    def __init__(self, first_name, last_name, gender, age, program, pay):
        super().__init__(first_name, last_name, gender, age)
        self.__program = program
        self.__pay = pay

    @property
    def program(self):
        return self.__program

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, new_pay):
        self.__pay = new_pay

    def __str__(self):
        return f"{self.full_name}  {self.gender}  {self.age}  {self.__program}  {self.__pay}"


programs = [{"program_name": 'math', "grade": 56}, {"program_name": 'english', "grade": 76}]
Suren = Student("Suren", "Parsyan", "male", 16, programs, 12, 5)
print(Suren.pass_exam(), Suren.exam_result)
