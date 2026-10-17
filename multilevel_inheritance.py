# Multilevel Inheritance

class Animal:
    def eat(self):
        print("Eating...")

class Mammal(Animal):
    def walk(self):
        print("Walking...")S

class Dog(Mammal):
    def bark(self):
        print("Barking...")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()
