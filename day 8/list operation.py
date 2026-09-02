# List Operations

l = [1, 3, 2, 4, 5, 64, 3]
print(l)

# id() - memory address of the list
print(id(l))

# append() - adds an element at the end
l.append(12)
print(l)

l.append(14)
print(l)

print(id(l))  # Same ID because list is mutable


# insert() - adds an element at a specific index
l.insert(1, 13)
print(l)


# extend() - adds multiple elements
l.extend([52, 34, 21])
print(l)

print(id(l))


# Indexing
print(l[3])


# pop() - removes an element using index
# l.pop(52) -> Error because 52 is not a valid index

print(l.pop(5))
print(l.pop())
print(l.pop(2))


# remove() - removes an element by value
l.remove(13)
print(l)


# del - deletes an element using index
del l[4]
print(l)


# clear() - removes all elements
l.clear()
print(l)


# List functions

l = [1, 3, 2, 4, 5, 64, 3]

print(max(l))
print(min(l))

# sorted() returns a new sorted list
print(sorted(l))
print(l)


# reverse() changes the original list
l.reverse()
print(l)


# sort() changes the original list
l.sort()
print(l)

# Sort in descending order
l.sort(reverse=True)
print(l)


# sum() - returns the total
print(sum(l))


# Two lists

l = [1, 4, 5]
m = [4, 7, 8]

print(l)
print(m)

m.append(10)

print(m)
print(l)


# all() and any()

print(all([1, '', [], (), set(), {}, False]))
print(any([1, '', [], (), set(), {}, False]))


# index() - returns the index of an element

# l.index(2) -> Error because 2 is not present

print(l.count(5))
print(l.count(4))


# Nested Lists

l = [
    [1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7]
]

print(l)

# Access first inner list
print(l[0])

# Access second inner list
print(l[1])

# Access element from nested list
print(l[0][2])
print(l[1][3])

# Negative indexing
print(l[-1][-1])