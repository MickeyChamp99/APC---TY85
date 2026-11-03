class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def show(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


e = Employee(101, "Amit", 20000)
m = Manager(102, "Rahul", 50000, "IT")

print("Employee Details:")
e.display()

print("\nManager Details:")
m.show()