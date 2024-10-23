class Student:

    class_year = 2024
    num_std = 0

    def __init__(self , name , age):
        self.name = name
        self.age = age
        Student.num_std += 1

    def details(self):
        print(f"{self.name}'s age is {self.age} his class has {Student.num_std} students and his graduating year is {Student.class_year}.")