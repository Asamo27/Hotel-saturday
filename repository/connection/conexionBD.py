from application.EmployeeService import EmployeeService
from domain.model.Employee import Employee
from repository.persistence.EmployeeRepository import EmployeeRepository


class EmployeeInput:
    def __init__(self):
        self.employee_service = EmployeeService()
        self.employee = Employee(None, None, None, None, None, None, None, None)
        self.employee_repository = EmployeeRepository()

    def register(self, employee, db):
        id_employee = input("Ingrese documento de identidad del empleado")
        self.employee.id = id_employee
        name = input("Ingrese su nombre")
        self.employee.name = name
        last_name = input("Ingrese su apellido")
        self.employee.last_name = last_name
        phone = input("Ingrese su numero de telefono")
        self.employee.phone = phone
        email = input("Ingrese su email")
        self.employee.email = email
        password = input("Ingrese su contraseña")
        self.employee.password = password
        status = input("Ingrese el estado")
        self.employee.status = status
        salary = input("Ingrese su salario")
        self.employee.salary = salary
        self.employee_repository.create_employee_repository(self.employee, db)

    def print_data(self):
        self.employee_service.print_employee_data()