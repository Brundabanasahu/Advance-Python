'''Q. Class Employee 
emp_name - public
emp_dept - protected
emp_salary - private

using get access salary
using set update salary by 3000'''

class Employee:

    def __init__(self, name, dept, salary):
        self.emp_name = name        # Public
        self._emp_dept = dept       # Protected
        self.__emp_salary = salary  # Private

    # Getter method
    def get_salary(self):
        return self.__emp_salary

    # Setter method
    def set_salary(self, amount):
        self.__emp_salary += amount


class Manager:

    def update_salary(self, employee):
        employee.set_salary(3000)
        print("Manager updated the salary.")

    
# Main Program
emp = Employee("Aditya", "IT", 50000)

print("Employee Name:", emp.emp_name)
print("Department:", emp._emp_dept)
print("Current Salary:", emp.get_salary())

mgr = Manager()
mgr.update_salary(emp)

print("Updated Salary:", emp.get_salary())
