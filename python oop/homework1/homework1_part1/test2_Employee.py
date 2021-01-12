class Employee:

    def __init__(self, id, first_name, last_name, position, salary, working_hours):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary
        self.working_hours = working_hours

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def annular_salary(self):
        return self.salary * 12

    def raise_salary(self, percent):
        return (self.salary + (self.salary / 100) * percent).__int__()


man = Employee(1, "Suren", "Parsyan", "position_1", 10500, "10:00-19:00")

print(man.full_name())

print(man.annular_salary())

print(man.raise_salary(10))
