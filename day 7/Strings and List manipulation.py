# String Methods

c = 'strings.py'

print(c.startswith('str'))
print(c.endswith('python'))
print(c.endswith('py'))

print(c.islower())
print(c.isupper())

print('Python'.isupper())
print('PYTHON'.isupper())
print('PYTHON12'.isupper())

print(c.isalpha())
print(c.isalnum())

print('s123'.isalnum())
print('s.123'.isalnum())

print('   '.isspace())
print('   k'.isspace())

print('this is total'.istitle())
print('This Is Title'.istitle())

print('my@var'.isidentifier())
print('_is'.isidentifier())


# List Operations

l = []
print(l)

l = list()
print(l)

l = [1, 2, 3.4, 5, [1, 2, 3], 'ert', {1: 2, 3: 8, 5: 7}]
print(l)

l = [34, 5, 7, 5, 3]
print(type(l))

m = [4, 5, 6, 7]

# List concatenation
print(l + m)

# List repetition
print(l + m * 3)

# List indexing
print(l[4])
print(l[-1])

# List slicing
print(l[2:])
print(l[:2])
print(l[::-1])