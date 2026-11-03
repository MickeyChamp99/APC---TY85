class Student:
    def calculate_grade(self):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self):
        marks = 85
        print("Engineering Grade: A" if marks >= 80 else "Grade: B")

class MedicalStudent(Student):
    def calculate_grade(self):
        marks = 75
        print("Medical Grade: A" if marks >= 70 else "Grade: B")

class ManagementStudent(Student):
    def calculate_grade(self):
        marks = 65
        print("Management Grade: A" if marks >= 60 else "Grade: B")

e = EngineeringStudent()
m = MedicalStudent()
s = ManagementStudent()

e.calculate_grade()
m.calculate_grade()
s.calculate_grade()