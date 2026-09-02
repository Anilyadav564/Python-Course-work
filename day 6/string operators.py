# String Basics

s = ''

print(s)

s = 'anilyadav'
print(s)

# String Concatenation
print(s + 'PFS')

# String Repetition
print(s * 10)

print('*' * 20)

print('-*-')
print('-*-' * 20)


# String Indexing

s = 'codegnan'

print(s[4])    # g
print(s[3])    # e
print(s[-2])   # a


# String Slicing

names = 'anil avinash ganesh'

print(names[0])     # a
print(names[7])     # i
print(names[-1])    # h
print(names[-4])    # e
print(names[3])     # l

# Slicing: [start:end:step]

print(names[12:20])  # ganesh
print(names[21:])    # Empty string
print(names[16])     # e
print(names[:-6])    # anil avinash

# Checking whether a string is present

print('anil' in names)       # True
print('avinash' in names)    # True
print('ravi' in names)       # False