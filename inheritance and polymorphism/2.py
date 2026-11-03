class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary:", 50000 + 10000)

class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary:", 40000 + 8000)

class Tester(Employee):
    def calculate_salary(self):
        print("Tester Salary:", 30000 + 5000)

m = Manager()
d = Developer()
t = Tester()

m.calculate_salary()
d.calculate_salary()
t.calculate_salary()