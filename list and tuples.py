Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# list  appending, insert, extended, modify,remove elements
l= [1,2,3,4,5]
l
[1, 2, 3, 4, 5]
id(l)
1369559514496
l.append(10)
id(l)
1369559514496
l.insert(1,12)
l
[1, 12, 2, 3, 4, 5, 10]
l.extend(30)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    l.extend(30)
TypeError: 'int' object is not iterable
l.extend([30,40,50])
l
[1, 12, 2, 3, 4, 5, 10, 30, 40, 50]
id(l)
1369559514496
l[2,60]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l[2,60]
TypeError: list indices must be integers or slices, not tuple
l([2,60])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l([2,60])
TypeError: 'list' object is not callable
l[3]
3
l
[1, 12, 2, 3, 4, 5, 10, 30, 40, 50]
id(l)
1369559514496
l.pop()
50
id(1)
140705013760936
l.pop()
40
id(l)
1369559514496
l
[1, 12, 2, 3, 4, 5, 10, 30]
l.remove(2)
l
[1, 12, 3, 4, 5, 10, 30]
id(l)
1369559514496
l
[1, 12, 3, 4, 5, 10, 30]
del.l[1]
SyntaxError: invalid syntax
del l[1]
l
[1, 3, 4, 5, 10, 30]
id(l)
1369559514496
l
[1, 3, 4, 5, 10, 30]
l.clear()
l
[]
id(l)
1369559514496
l=[1,2,3,4,10,20,]
max(l)
20
min(l)
1
l
[1, 2, 3, 4, 10, 20]
sorted(l)
[1, 2, 3, 4, 10, 20]
l
[1, 2, 3, 4, 10, 20]
l.reverse()
l
[20, 10, 4, 3, 2, 1]
l.sort()
l
[1, 2, 3, 4, 10, 20]
l.sort(reverse=True)
l
[20, 10, 4, 3, 2, 1]
sum(l)
40
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
m
[1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
n=1
n.append(6)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    n.append(6)
AttributeError: 'int' object has no attribute 'append'
n=l
n.append(4)
l
[1, 2, 3, 4, 5, 4]
m
[1, 2, 3, 4, 5]
m=l
m
[1, 2, 3, 4, 5, 4]
m=l.copy()
m
[1, 2, 3, 4, 5, 4]
m.append(10)
m
[1, 2, 3, 4, 5, 4, 10]
l
[1, 2, 3, 4, 5, 4]
all([0,'',[],set(),{},false])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    all([0,'',[],set(),{},false])
NameError: name 'false' is not defined. Did you mean: 'False'?
all([0,'',[],,(),set(),{},false])
SyntaxError: invalid syntax
all([0,'',[],(),set(),{},false])
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    all([0,'',[],(),set(),{},false])
NameError: name 'false' is not defined. Did you mean: 'False'?
false
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    false
NameError: name 'false' is not defined. Did you mean: 'False'?
all([0,'',[],(),set(),{},false])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    all([0,'',[],(),set(),{},false])
NameError: name 'false' is not defined. Did you mean: 'False'?
all([0,'',[],(),set(),{},False])
False
all([1,'',[],(),set(),{},False])
False
any([1,'',[],(),set(),{},False])
True
l
[1, 2, 3, 4, 5, 4]
l.index(3)
2
l
[1, 2, 3, 4, 5, 4]
l
[1, 2, 3, 4, 5, 4]
l.count(3)
1
>>> l.count(6)
0
>>> l=([],[[])
...    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> l=([1,2,3,4][1,2,3,4])
...    
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    l=([1,2,3,4][1,2,3,4])
TypeError: list indices must be integers or slices, not tuple
>>> l=[[1,2,3,4][1,2,3,4]]
...    
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    l=[[1,2,3,4][1,2,3,4]]
TypeError: list indices must be integers or slices, not tuple
>>> l=[[1,2,3,4],[1,2,3,4]]
...    
>>> l
...    
[[1, 2, 3, 4], [1, 2, 3, 4]]
>>> l[0]
...    
[1, 2, 3, 4]
>>> l[1]
...    
[1, 2, 3, 4]
>>> l[0][2]
...    
3
>>> l[1][3]
...    
4
>>> l[-1][-1]
...    
4
>>> #tuple
...    
