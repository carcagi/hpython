class student():
    academy = 'Holberton'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__year = 2021  # Considered private

    def description(self):
        return f"{self.name}, is at {self.academy}, has {self.age} years"

    # Function str helps replacing the output when you print the object
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def complain(self):
        return f"{self.name}, is is complaining"


class studentCH13(student):

    _protection = True  # Considered protected

    def cohort(self):
        return f"{self.name} is currently in CH 13."

    def description(self, company):
        self.company = company
        return f"{self.name} works at {self.company}"

    # Simple setter for _protection
    def set_protection(self, param):
        self._protection = bool(param)

    # Simple getter for _protection
    def get_protection(self):
        return self._protection


student1 = studentCH13('Pepito', 21)
student1.name = "Juanita"
student1.year = 2020
print(student1.description('GOOGLE'))
print(student1.year)
