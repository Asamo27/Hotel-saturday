from domain.model.Employee import Employee

class EmployeeService:
    register_employee = []

    def __init__(self):
        self.employee = Employee(None, None,None,None, None,None, None, None)

    def create_employee(self, employee):
        employee.id_employee = self.register_employee[0]
        employee.name = self.register_employee[1]
        employee.last_name = self.register_employee[2]
        employee.phone = self.register_employee[3]
        employee.email = self.register_employee[4]
        employee.password = self.register_employee[5]
        employee.status = self.register_employee[6]
        employee.salary = self.register_employee[7]

    def print_employee_data(self=None):
        for employee in self.register_employee:
            print(employee)