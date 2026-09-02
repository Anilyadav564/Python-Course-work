# Dictionary Operations

data = {
    'name': 'krishna',
    'batch': 63,
    'course': 'PFS'
}

# Accessing values

print(data['name'])
print(data['batch'])
print(data['course'])


# Checking keys

print(63 in data)       # False

# data['age']            # KeyError

print(data.get('age', 'key is not present'))
print(data.get('course', 'key is not present'))


# Updating a value

data['batch'] = 64
print(data)


# Adding a new key-value pair

data['skills'] = ['python', 'mysql', 'flask']
print(data)

data['age'] = 21
print(data)


# Adding multiple key-value pairs

data.update({
    'phno': 98432683134,
    'email': 'example@gmail.com'
})

print(data)


# Removing a key using pop()

print(data.pop('age'))
print(data)


# Removing a key using del

del data['name']
print(data)


# Removing the last inserted item

print(data.popitem())
print(data)


# Remove another last item

print(data.popitem())
print(data)


# Clear the dictionary

data.clear()
print(data)