# Input Operations in Python


# Taking a single input

x = input()
print(x)

name = input()
print(name)


# Taking input with a message

name = input("Enter your name: ")
print(name)


# Taking integer input

age = int(input("Enter your age: "))
print(age)
print(type(age))


# input() always returns a string

age = input("Enter age: ")
print(age)
print(type(age))


# Taking multiple names

names = input("Enter names: ")
print(names)

# split() separates the string into elements
print(names.split())


# Taking names as a list

names = input("Enter names: ").split()
print(names)


# Taking numbers as input

names = input("Enter numbers: ").split()
print(names)

# Convert strings into integers
numbers = list(map(int, names))
print(numbers)


# Taking multiple integer values directly

values = list(map(int, input("Enter numbers: ").split()))
print(values)


# Taking names as a tuple

names = tuple(input("Enter names: ").split())
print(names)

print(list(names))
print(set(names))


# Taking names as a set

names = set(input("Enter names: ").split())
print(names)

print(list(names))
print(tuple(names))
print(set(names))
print(str(names))


# Using map() with strings

names = set(map(str, input("Enter names: ").split()))
print(names)


# Taking multiple inputs

a, b = [1, 2]

print(a)
print(b)


# Taking email and password

email, password = input(
    "Enter the mail and password: "
).split()

print(email)
print(password)


# Taking multiple integer inputs

a, b, c = list(map(int, input("Enter three numbers: ").split()))

print(a)
print(b)
print(c)


# Taking name and marks

name, marks = input("Enter name and marks: ").split()

print(name)
print(marks)

print(int(marks))


# Using eval()

e = eval(input("Enter a value: "))

print(e)
print(type(e))