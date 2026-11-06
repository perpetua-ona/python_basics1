import math
import random
from fractions import Fraction
from functools import reduce

""" The docstring 
    A docstring is a string literal that appears as the first statement in a module, 
    function, class, or method definition. It is used to document the purpose and 
    usage of the code element.
"""


# varibles and datatypes 

# a variable is a named container used to store and manage data in a computer's memory

# eg
# name_of_person = 20 


# import random

# print(__doc__)

# number2 = 5
# print(type(number2))

# course = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#             Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
# print(type(course))
# if "o" in course:
#     print(course)


# NUMBER2 = 1000

# Python basic operations
#  arithmetic, comparison and logical operations
#  - arithemetic operations: +, -, , /, %, *, //
#  - comparison operations: ==, !=, >, <, >=, <=
#  - logical operations: and, or, not
#  - identity operations: is, is not
#  - membership operations: in, not in

# import math


# num = 40


# add = num + 30
# sub = num - 30
# mutiply = num * 30
# div = num / 30
# modulos = num % 30
# floor_division = num // 30
# power = num ** 30

# print("AA" + "BB")
# print(add)
# print(sub)
# print(mutiply)
# print(div)
# print(modulos)
# print(floor_division)
# print(power)
# print(10/3)
# print(math.ceil(10/3))
# print(math.floor(10/3))


# - comparison operations: ==, !=, >, <, >=, <=

# b = int(input("b =>>>"))
# if a>b:
#     print("Hello")
# else:
#     print("Hi")

#  - logical operations: and, or, not

# school = input("Enter your school name")
# if (school == "MODEL") or (school == "NHS"):
#     print("You are qualified")
# else:
#     print("Print you are not qualified")


# name = 20
# if not(name == "Paul"):
#     print(f"Hello {name}")
#     # print(name+ " nano")
#     print("Name is not Paul")



# Week 2: Data Types and Operations
# • Strings: formatting, indexing, slicing, methods
# • Numbers: integers, floats, complex numbers, mathematical operations
# • Booleans: logical operations, conditional statements

# course = input("Enter your course name: ")
# age = input("Enter your age: ")

# string escape sequences
#   - \n: newline
#   - \t: tab
#   - \b: backspace
#   - \r: carriage return
#   - \f: form feed
#   - \": double quote
#   - \': single quote
#   - \\: backslash


# no = 1000000000000.5040

# string = f'I am {no:,} years old\\ and I am studying java'
# print(string)



# What is indexing

# indexing is the process of accessing an individual element
# within a sequence—such as a string, list
# or tuple—by referring to 
# its specific position number


# string = "Hello world is a common term in programming"

# print(string)
# # print(string.find("o"))
# # print(string[8])

# # slicing
# # print(len(string))
# # print(string[-43])


# # print(string.split())


# # string methods 
# # capitalize() casefold() center() count()
# # endswith() find() format() index()
# # isalpha() isdigit() join() lower() replace() split() strip()

# #this displays the number of m in string
# # print(string.count("m"))

# # Numbers: integers, floats
# # complex numbers, mathematical operations

# # +, -, *, /, //, %, **

# # print(4**2)

# comp1 = 5+2j 

# comp2 = 5+6j

# # print(comp1 * comp2)

# num = 10
# print(math.pi)
# rad = math.radians(num)
# print(math.cos(rad))
# print(math.sin(rad))
# print(math.tan(rad))

# print(rad)

# # print(math.exp(30))
# print(math.pow(2, 3))
# print(math.floor(5/2))
# print(math.ceil(5/2))

# print(random.randint(1, 100))
# print(random.choice(["Hello", "Hi", "Hey"]))
# print(random.sample(["Hello", "Hi", "Hey", 3, 4,5], 3))
# print(random.uniform(1, 10))
# print(random.choices(["Hello", "Hi", "Hey", 3, 4, 5], k=2))
# list1 = ["Hello", "Hi", "Hey", 3, 4,5]
# print(random.shuffle(list1))
# print(list1)
# print(5/2)
# print(2/3)

# fac = Fraction("2/3")

# print(fac)

# # Booleans: logical operations, conditional statements, comparison operations
# print(1==1)
# print(1==11)


# print(int(True))
# print(int(False))

# # Booleans: logical operations, conditional statements, comparison operations

# is_student = bool(input("Are you a student: "))
# name = input("Enter your name: ")


# if is_student == True or name=="victor":
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student")


# jmdata = {
#     "name": "jm",
#     "age": 20,
#     "course": "Python"
# }



# # Python data structures are specialized containers used 
# # to organize, store, manage, and manipulate collections of
# # data efficiently in computer memory


# str
# str, int, float, bool, complex, list, tuple, dict
# numbers = range(1,10)

# list1 = ["JM", "Paul", 20, True, 5+2j, 5/2, 1==1, 5.5]
# list2 = list(numbers)


# appen = list1.append("Python")

# print(list2)
# print(list1)

# tuples = tuple(numbers)

# print(tuples)


# kwargs = dict(name="paul", age=20, course="Python")

# dict1 = {
# "name": "JM",
# "age": 20,
# "course": "Python"
# }
# dict2 = dict(kwargs)


# print(dict1)
# print(kwargs)
# print(dict3)

# dict

# name = "p,r,o,g,r,a,m,m,i,n,g"

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])

# print(name[-3])
# print(name[-2])
# print(name[-1])

# list1 = ["JM", "Paul", 20, False, 5+2j, 5/2, 1==1, 5.5]
# tuple1 = ("JM", "Paul", 20, True, 5+2j, 5/2, "Many", 5.5)
# # 

# list2 = list1[:]

# print(list2)
# print(tuple1[:])


# print(list1[0], list1[3])
# print(tuple1[0], tuple1[5])

# dict, str, list, tuple, int, float

# # dictionary methods
# pop() , copy(), popitem(), items(), get(), keys(), values(), update(), fromkeys(), setdefault()


# dict3 = dict([["name", "JM"], ["age", 20], ["course", "Python"]])
# print(dict3)

# dict1 = {}

# print(dict1.fromkeys(["name", "age", "course"], "Nano"))

# new = dict3.setdefault("new", "Nano")
# print(new)
# print(dict3)

# print(dictionar2)



# List Methods
# append() clear() copy() count() extend() insert() remove() 
# pop() index(), reverse() sort()

# list1 = [3,4,0,7,20,15]
# tuple1 = ("JM", "Paul", 20, True, 5+2j, 5/2, "Many", 5.5)

# # listappend = list1.append("Python")
# print(list1)

# # listclear = list1.clear()
# print(list1)

# listextend = list1.extend([1,2,3,4,5])
# print(list1)

# listinsert = list1.insert(1, "JM")
# print(list1)

# listremove = list1.remove("JM")
# print(list1)

# listpop = list1.pop()
# print(list1)

# listreverse = list1.reverse()
# print(list1)

# listsort = list1.sort()
# print(list1)

# listcopy = list1.copy()
# print(listcopy)

# listcount = list1.count(20)
# print(listcount)

# listindex = list1.index("JM")
# print(listindex)

# tuple1 = ("JM", "Paul", 20, True, 5+2j, 5/2, "Many", 5.5, "JM")

# tupleops = tuple1.index("Paul")
# print(tupleops)
# tuplecount = tuple1.count("Paul")
# print(tuplecount)


# In computer programming, control flow refers to the exact order in which individual statements
# instructions, or function calls are executed within a program.

# 3 Types of control flows or structures

# - Sequence
# - Selection/Conditional
# - Iteration/Repetition


# sequence of expressions/statements
# print(age3)
# name1 = "Obinna"
# name2 = "Paul"
# name3 = "John"
# amount = 5000
# amount2  = 1000
# no_amount  = 0
# # print(age3)
# # print(age2)
# # print(age)
# # print(name3)
# # print(name2)
# # print(name1)


# #  if, else, elif
# my_money = int(input("How much do you have: "))

# if my_money >= amount:
#     print("Buy Ozu Okuko")
# elif my_money >= amount2 and my_money < amount:
#     print("Buy Ugu make we cook")
# else:
#     print("Nothing to buy")
    

# Iteration/Repetition

# list1 = ["name", "paul", 1, 10, 100]


# for item in list1:
#     print(item)

# while loop

# i = 0
# while i <= 10:
#     print(i)
#     i += 1


# for i in listofbooks:
#     if "c" in i.lower():
#         print(i.lower())
#     else:
#         print(i.upper())


# listofbooks = ["python", "java", "c++", "javaScript", "c#"]
# bookprices = [500, 1000, 1500, 2000, 2500]

# bookinterest = input("What book are you interested in: ")

# bookandprices = dict(zip(listofbooks, bookprices))
# # print(bookandprices)
# print(bookandprices.keys())
# # amount = 20
# if bookinterest in listofbooks:
#     amount = int(input("How much do you have: "))
#     if amount >= bookandprices.get(bookinterest):
#         print("you can make payment") 
#     else:
#         print("Your money is not enough")
# else:
#     print("Book is not avaliabel")

# print(amount)
# break, continue, pass
# # loop control statements

# listofnumbers = list(input("enter your list of names: "))

# for i in listofnumbers:
#     if i == "m":
#         break
#     print(i)



list5 = [5,2,1,9,44,32,11,56,21]

dict1 = {"name": "jm", "age": 20, "course": "Python"}
# List comprehension
# This is the concept of writing for loop in a single line to create a list from an existing list
# for num in list5: 
#     print(num)


# print(dict1.items())
# print(dict1.keys()[0:1])

newlist = [num for num in list5 if num %2 ==0]
# dict2 = {a.upper():r for a, r in dict1.items() if type(r) == str}
# print(dict2) 
# # print(list5)
# print(newlist)

 

# A function is a self-contained, reusable block of code designed to perform a specific task.
# Think of it as a mini-program or a "machine" within a larger program: you feed it information,
# it processes that information, and it gives you back a result

# A function parameter is a variable that  the values that a function needs
# for execution at the place of function definition.
# amount = 10
# def name(a,b):
#     print(amount)
#     if b == 0:
#         return "Numbers cannot be zero"
#     return a/b
# print(name(10,5))

# name(12, 6)


# print("Hello", 123, "Excel", "Victor")


list2 = [ "name", "no", "Hello", True]


def function2(*args,**kwargs):
    global list1
    list1 = list(args)
    list1.extend(list2)
    list1 = [num for num in list1 if num %2 ==0]
    
    dict1 = {a.upper():r for a, r in kwargs.items() if type(r) == str}
#     return list1, dict1

# function2(12, 6, 10, 44, 2, 5.5, False, name=12, l=6, z="Hello")

# print(list1)






# Lambda functions
# lambda functions are small anonymous functions that can have any 
# number of parameters/arguments but only one expression, we can use for quick computation in our programs


# lambda arguments: expression

var = lambda a: random.randint(a, 20)
print(var(5))
# function2(1,2,3)
# list2 = ["Name", "No", "Nxtel", "leo"]

# funct = lambda a: a.startswith("N")

# # filter
# filtered = list(filter(function3,list1))
# print(filtered)


# reduce function applies a cumulative action to the items of an iterable from left to right.

# def function3(a,b):
#     return a*b

# list1 = [4,8,12,16,20,24,28,32,36,40]


# reduceed = reduce(function3,list1)
# print(reduceed)


