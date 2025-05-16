from domain.model.Employee import Employee

class EmployeeRepository:
    def __init__(self):
        self.employee = Employee

    def create_employee_repository(self, employee, db):
        query = "INSERT INTO Employee (id_employee, name, last_name, phone,  email, password, status, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (employee.id, employee.name, employee.last_name,employee.phone,employee.email, employee.password, employee.status, employee.salary)
        db.execute_query(query, values)

    def find_all_employees(self, db):
        query = "SELECT * FROM employee"
        response = db.execute_query(query)
        return response


    def update(self, employee, db):
        query = "UPDATE Employee SET name = %s, last_name = %s, phone = %s, email = %s, password = %s, status = %s, salary = %s WHERE id_employee = %s"
        values = (employee.name, employee.last_name, employee.phone, employee.email, employee.password, employee.status, employee.salary, employee.id)
        return db.execute_query(query, values)

    def delete(self, id_employee, db):
        query = "DELETE FROM Employee WHERE id_employee = %s"
        values = (id_employee,)
        response = db.execute_query(query, values)
        return response