#Generators 🚰
'''A generator is like a water tap.

A list gives all water at once 🪣
A generator gives one drop when you ask 💧'''
#Generators 🚰:
'''A generator is a special Python function
""" that gives values one at a time using yield, instead of giving 
    all values together. 🚰"""
#Generator function: gives one number at a time
'''def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
data = numbers()
for value in  data:
    print(value)'''
#yield pauses and waits. 
# for or next() tells it to start giving values.  
'''def display():
    yield "Anil"
    yield "python"
    yield "java"
data = display()
print(next(data))
print(next(data))
print(next(data))'''
'''first next(data)  → Anil
second next(data) → python
third next(data)  → java
After "Anil" is given, Anil pauses. It does not start again from the top.'''
#Generator with a loop: even numbers
'''def even_numbers():
    for i in range(2,11,2):
      # range(start, stop, jump): 
         yield i
for num in even_numbers():
    print(num)   '''    
#Important: generator can finish 🛑
'''def demo():
    yield 10 
    yield 20
g = demo()
print(next(g))
print(next(g))
print(next(g))
First two next() calls work:
10
20
But there are only two values. The third next(g) causes:
StopIteration
It means: “No more values are left.”
Easy rule:
yield = give one value and pause
next() = ask for the next value
for loop = keeps asking automatically until finished'''









