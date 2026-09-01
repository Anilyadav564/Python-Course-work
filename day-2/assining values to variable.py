#variable
#A variable is a name used to store a value.
#e
name = "Anil"
age = 20
marks = 85.5
'''| Variable | Value stored |
|---|---|
| `name` | `"Anil"` |
| `age` | `20` |
| `marks` | `85.5` |'''
#= means assign: put the value on the right into the variable on the left.
# Single assignment
name = "Anil"

# Multiple variables, different values
a, b, c = 10, 20, 30

# Multiple variables, same value
x = y = z = 100

# Change (reassign) a variable
age = 20
age = 21

# Swap values
a = 5
b = 10

a, b = b, a
print(a, b)  # 10 5
#ex for clear
name = "Anil"
age = 20
marks = 85

print("Name:", name)
print("Age:", age)
print("Marks:", marks)

age = 21
print("Updated age:", age)

a, b = 5, 10
a, b = b, a
print("After swap:", a, b)