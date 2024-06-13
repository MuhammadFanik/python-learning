import random

# Variables
# num1 = 5
# num2 = 7
# first_name = "Sam"
# last_name = "Smith"
# print(num1, num2)  # Output: 5 7
# print(num1 + num2)
# print(first_name + last_name)
# # If you try to print the string and a number with the + operator, it will give you an error, Use comma instead.
# print("Integer and string combined", num1, first_name)


# Casting
# strNum = str(3)
# intNUm = int(3)
# floatNum = float(3)
#
#
# # type checking
# print(type(strNum))
# print(type(intNUm))
# print(type(floatNum))


# Data Types
    # Text: str
    # Numeric: int, float, complex
    # Sequence: list, tuple, range
    # Mapping: dictionary
    # Set types: set, frozenset
    # boolean type: bool


# Numbers
# intNum = 3
# floatNumber = 3.6
# complexNumber = 6 + 5j
#
# print(type(intNum))
# print(type(floatNumber))
# print(type(complexNumber))
# print(random.randrange(1, 10)) # Printing a random number
#
#
# # Booleans
# print(5 > 3)
# # Any string is true, except empty ones
# # all numbers are true, except 0
# # Any list, tuple, set and dict are true, except empty ones
#
# print(bool(7))


# Logical Operators: and, or,  not
print((3 < 5) and (5 > 7))
print((3 < 4) or (5 > 7))
print(not((7 < 9) and (9 > 6)))

# Arithmetic Operators: +, -, *, /, %, **, //
# num1 = 7;
# num2 = 3;
# print(num1 + num2)  # 10
# print(num1 - num2)  # 4
# print(num1 * num2)  # 21
# print(num1 / num2)  # 2.3333
# print(num1 ** num2)     # 343
# print(num1 % num2)  # 1
# print(num1 // num2)     # 2
#
# # Assignment Operators: =, +=, -=, *=, /=, %=, //=,
# # Comparison Operators: ==, <, >, <=, >=, !=
#
# # Membership Operators : in, not in
# message = "This is a python lecture"
# print("Java" in message)    # False
# print("Class" not in message)   # True

# Bitwise Operators (used to compare binary numbers)
# bitNum1 = 6
# bitNum2 = 2
# print(bitNum1 & bitNum2)    # 110 & 10  ===>  10 ===> 2
# print(bitNum1 | bitNum2)    # 110 | 10  ===>  110 ===> 6
# print(bitNum1 ^ bitNum2)    # 110 ^ 10  ===>  100 ===> 4
# print(~bitNum1)     # -(num + 1)
# print(bitNum1 << 2)
# print(bitNum1 >> 2)


# Identity operators: is, is not (discussed later)


# If..elif..else
x = 10;
y = 10
if(x > y):
    print("x is greater than y")
elif(x < y):
    print("x is less than y")
else:
    print("This is else statement")

# If statements cannot be empty, but if you have an if statement with no content, put in the pass statement
if(10 > 9):
    pass
print("Hello")
