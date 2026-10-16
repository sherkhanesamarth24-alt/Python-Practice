# Instance and Class Variables

class Student:
    college = "DY Patil Technical University"

    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("Samarth", "AIML")
student2 = Student("Rahul", "CSE")

print(student1.name, "-", student1.course)
print(student2.name, "-", student2.course)
print("College:", Student.college)
