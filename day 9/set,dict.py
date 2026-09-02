# Set Operations

s = set()
print(s)

s = {1, 2, 3, 5, 6, 4, 7, 8, 9, 25, 36}
print(s)
print(type(s))

# Adding elements
s = set()
s.add(1)
s.add(12.3)
s.add(2 + 4j)
print(s)

# Duplicate values are removed
s = {1, 1, 1, 1, 1, 1}
print(s)


# Set does not support + operator

l = {10, 20, 30}
m = {1, 2, 3, 4}

# l + m  # TypeError


# Set operations

a = {1, 2, 3, 4, 5}
b = {3, 5, 7, 9}

print(a | b)       # Union
print(a & b)       # Intersection
print(a - b)       # Difference
print(a ^ b)       # Symmetric Difference

print({1} <= a)    # Subset

print(a.isdisjoint(b))
print(a.isdisjoint({9, 10}))

print(a.union(b))
print(a.intersection(b))
print(a.issubset(b))
print(a.issuperset(b))


# Membership
print(5 in a)

# Maximum, Minimum and Sorting
print(max(a))
print(min(a))
print(sorted(a))


# Assignment and Copy

b = a
b.add(12)

print(a)
print(b)

c = a.copy()
c.add(13)

print(a)
print(c)


# discard()
a.discard(12)
a.discard(5)
print(a)


# clear()
a.clear()
print(a)


# update()
a = {1, 2, 3, 4, 5, 12}

a.add(123)
a.update({16, 17, 18})

print(a)


# pop()
print(a.pop())
print(a.pop())
print(a.pop())


# remove()
a.remove(16)
print(a)

a.remove(12)
print(a)


# Length, all() and any()

a = {1, 2, 3, 4, 5}
a.update({"str", 0, 12, 13, -1, -23.4})

print(a)
print(len(a))
print(all(a))
print(any(a))


# Frozen Set

a = frozenset({1, 12, 13, 10, 18, 59, 20})
print(a)

# a.add(12)  # Error because frozenset is immutable


# ==================================================
# Dictionary Operations
# ==================================================

d = {}
print(d)

d = dict()
print(d)
print(type(d))


# Creating a dictionary

d = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3'
}

print(d)
print(id(d))


# Adding a new key-value pair

d['k4'] = 'v4'
print(d)
print(id(d))


# Dictionary with different types of keys

d = {}

d[1] = 'int'
d[12.3] = 'flt'
d[2 + 6j] = 'com'
d['str'] = 'string'
d[(1, 2, 3, 4)] = 'tuple'

print(d)


# Dictionary with different types of values

d = {}

d[1] = 1
d[2] = 12.3
d[3] = 3 + 90j
d[4] = 'Moksha'
d[5] = [1, 2, 3, 4, 3]
d[6] = (3, 4, 5, 6)
d[7] = {1, 2, 3}
d[8] = {1: 4}

print(d)


# Membership checks keys, not values

print(9 in d)
print(8 in d)
print('Moksha' in d)


# Accessing values

print(d[5])
print(d[8])


# Updating values

d[3] = 4
d[5] = 190
d[6] = 12
d[7] = [1, 2, 3, 4, 5, 67]

print(d)