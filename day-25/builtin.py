import sys
print(sys.version)
print(sys.path)
print('Start')
sys.exit()
print('end')

import platform
print(platform.system())
print(platform.release())
print(platform.processor())

import math
print(math.pi)
print(math.e)
print(math.sqrt(36))
print(math.pow(7,6))
print(math.ceil(12.0002))
print(math.ceil(12.3))
print(math.ceil(12.6))
print(math.ceil(12.99))
print(math.floor(11.00008))
print(math.floor(12.3))
print(math.floor(14.6))
print(math.floor(15.99))

print(math.fabs(-54))
print(math.factorial(7))
print(math.gcd(5,120))
print(math.log(2,6))
print(math.sin(45))
print(math.cos(30))
print(math.tan(45))
print(math.degrees(30))
print(math.radians(30))

import random as r
#r.seed(10)
print(r.randint(1,13))
print(r.randint(100000,999999))
print(r.random())
print(r.uniform(1,6))
l=['R','P','S']
print(r.choice(l))
print(r.choices(l,k=2))
r.shuffle(l)
print(l)

from collections import Counter, defaultdict, deque
s='Python Programming'
m='this is that that is this is is'.split()
l=[1,1,1,5,5,5,5,8,8,8,8,9,45]
print(Counter(s))
print(Counter(l))
print(Counter(m))
print(Counter(m)['is'])

d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)

l=deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()
print(l)

l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(70)
l.pop()
print(l)

from itertools import permutations, combinations

res1=list(combinations('abc',2))
res2=list(permutations('abc',2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])