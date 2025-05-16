from domain.model.User import User


class Employee(User):

    def __init__(self, id_employee, name, last_name, phone, email, password, status, salary):
        super().__init__(id_employee, name , last_name, phone, email, password, status)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def __str__(self):
        return f"salary: {self._salary}"