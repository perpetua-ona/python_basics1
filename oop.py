
# Encapsulation is binding data and methods that operate on the data together.

# class Students:
#     ssl = 12
#     def __init__(self, name, age, course):
#         self.__name = name
#         self.age = age
#         self.course = course
#     def student_name(self):
#         return f"Hello {self.name}"
#     @classmethod
#     def get_ssl(cls, a):
#         newssl =  cls.add_numbers(a) + cls.ssl
#         return newssl
#     @staticmethod
#     def add_numbers(b):
#         return 12+b
    
#     @property
#     def name(self):
#         # newname =  +"Nano"
#         return self.__name   
#     @name.setter
#     def name(self, name):
#         self.__name = name
    
# student1 = Students("JM", 20, "Nano")
# print(student1.name)

# student1.name = "Simeon"
# print(student1.name)


# inheritance, polymorphism and abstraction

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f"Hello {self.name} you are {self.age} years old"

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def info(self):
        return f"Hi {self.name} you are {self.age} years old and you are a student"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def info(self):
        return f"Hello {self.name} you are {self.age} years old and you are a teacher"


person = Person("Nano", 34)
student = Student("JM", 20, "Nano")
teacher = Teacher("Nano", 34, "Math")

typesofpeople = [student, teacher, person]

for i in typesofpeople:
    print(i.info())





