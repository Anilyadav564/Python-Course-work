import keyword
print(keyword.kwlist)#list of all keywords
print(len(keyword.kwlist))#total number of keyword
'''| Keyword | Simple meaning |
|---|---|
| `False` | Represents a false condition/value. |
| `None` | Represents no value or an empty value. |
| `True` | Represents a true condition/value. |
| `and` | True only when both conditions are true. |
| `as` | Gives another name while importing or using something. |
| `assert` | Checks a condition and gives an error if it is false. |
| `async` | Creates an asynchronous function. |
| `await` | Waits for an asynchronous task to finish. |
| `break` | Immediately stops a loop. |
| `class` | Creates a class. |
| `continue` | Skips the current loop turn and goes to the next one. |
| `def` | Creates a function. |
| `del` | Deletes a variable or item. |
| `elif` | Checks another condition after `if`. |
| `else` | Runs when the `if` condition is false. |
| `except` | Handles an error from `try`. |
| `finally` | Runs whether an error happens or not. |
| `for` | Repeats code for each item. |
| `from` | Imports a specific item from a module. |
| `global` | Uses a global variable inside a function. |
| `if` | Runs code only when a condition is true. |
| `import` | Brings a module into the program. |
| `in` | Checks whether an item exists in something. |
| `is` | Checks whether two variables refer to the same object. |
| `lambda` | Creates a small one-line function. |
| `nonlocal` | Uses a variable from the nearest outer function. |
| `not` | Reverses True to False, or False to True. |
| `or` | True when at least one condition is true. |
| `pass` | Does nothing; used as a placeholder. |
| `raise` | Creates/throws an error intentionally. |
| `return` | Sends a value back from a function. |
| `try` | Runs code that may cause an error. |
| `while` | Repeats code while a condition is true. |
| `with` | Safely works with resources such as files. |
| `yield` | Returns values one at a time from a function. |'''
##
# False
is_raining = False
# None
result = None
# True
is_logged_in = True
# and
age = 20
if age > 18 and age < 60:
    print("Adult")
# as
import math as m
print(m.sqrt(16))
# assert
age = 20
assert age >= 18
# async and await
import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello")

asyncio.run(hello())
# break
for number in range(5):
    if number == 3:
        break
    print(number)
# class
class Student:
    name = "Anil"
# continue
for number in range(5):
    if number == 2:
        continue
    print(number)
# def
def greet():
    print("Hello")

greet()
# del
name = "Anil"
del name
# if, elif, else
marks = 75

if marks >= 90:
    print("A Grade")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
# try, except, finally
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
finally:
    print("Program ended")
    # for
for fruit in ["apple", "mango"]:
    print(fruit)
    # from
from math import sqrt
print(sqrt(25))
# global
count = 0

def increase():
    global count
    count = count + 1

increase()
print(count)
# import
import math
print(math.pi)
# in
fruits = ["apple", "mango"]

if "mango" in fruits:
    print("Mango found")
# is
a = [1, 2]
b = a

print(a is b)  # True
# lambda
square = lambda number: number * number
print(square(5))
# nonlocal
def outer():
    number = 10

    def inner():
        nonlocal number
        number = 20

    inner()
    print(number)

outer()
# not
is_raining = False

if not is_raining:
    print("Go outside")
# or
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
# pass
def future_function():
    pass
# raise
age = -2

if age < 0:
    raise ValueError("Age cannot be negative")
# return
def add(a, b):
    return a + b

print(add(2, 3))
# while
number = 1

while number <= 3:
    print(number)
    number = number + 1
# with
with open("notes.txt", "w") as file:
    file.write("Hello")
# yield
def numbers():
    yield 1
    yield 2

for number in numbers():
    print(number)
# match and case
day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Other day")