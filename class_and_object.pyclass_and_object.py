# Class and Object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


student1 = Student("Samarth", 21)
student1.display()
