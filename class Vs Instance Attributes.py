class Student:
    school = "MIT"  # Class attribute

    def __init__(self, name, course):
        self.name = name  # Instance attribute
        self.course = course  # Instance attribute

# Creating two student objects
student1 = Student("Alice", "Computer Science")
student2 = Student("Bob", "Physics")

# Accessing class attribute
print(Student.school)  # Output: MIT
print(student1.school)  # Output: MIT
print(student2.school)  # Output: MIT

# Accessing instance attributes
print(student1.name)  # Output: Alice
print(student2.course)  # Output: Physics
