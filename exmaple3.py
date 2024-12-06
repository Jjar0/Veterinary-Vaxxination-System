# Parent Class
class Student:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I dont know who I am"

# Child Classes inherit from 'Student'
class Sam(Student):
    def speak(self):  # Polymorphism overriding the parent class method
        return "My name is Sam"

class Will(Student):
    def speak(self): 
        return "My name is Will"

# Using Inheritance and Polymorphism
students = [Sam("Sam"), Will("Will"), Student("X")]

for student in students:
    print(f"{student.name} says {student.speak()}")