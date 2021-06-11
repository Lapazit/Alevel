class Human:
    # TODO: name, surname, str(Human) -> Name Surname
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f"{self.name} {self.surname}"
class Employee(Human):
    # TODO: salary, get_paid -> sum of money to be paid
    def __init__(self, name, surname, salary):
        super().__init__(name, surname)
        self.salary = salary
        self.paid = 0
    def __str__(self):
        return f"{self.name} {self.surname} {self.salary}"
    def get_paid(self):
        self.paid += self.salary
        return self.paid
class Programmer(Employee):
    # TODO: programming language, bonus
    def __init__(self, name, surname, salary, language, bonus):
        super().__init__(name, surname, salary)
        self.language = language
        self.bonus = bonus
    def get_paid(self):
        return super().get_paid() + self.bonus
class Manager(Employee):
    # TODO: title, multiplication_k
    def __init__(self, name, surname, salary, title, multiplication_k):
        super().__init__(name, surname, salary)
        self.title = title
        self.multiplication_k = multiplication_k
    def get_paid(self):
        return super().get_paid() * self.multiplication_k
employees = [Programmer('Anton', 'Martynov', 1000, 'python', 100),
             Manager('Kyrylo', 'Kozhemyaka', 2000, 'java', 1.2),
             Employee('Sam', 'Smith', 800)]
# l=Programmer('Anton', 'Martynov', 1000, 'python', 100)
# l.bonus()
for e in employees:
    print(f"{e} have to be paid: {e.get_paid()}")