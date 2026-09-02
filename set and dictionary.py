Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#set
s={}
type(s)
<class 'dict'>
set=set()
s={1,2,3,45,6,7,89}
s
{1, 2, 3, 6, 7, 89, 45}
s=set()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s=set()
TypeError: 'set' object is not callable
s
{1, 2, 3, 6, 7, 89, 45}
set()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set()
TypeError: 'set' object is not callable
s
{1, 2, 3, 6, 7, 89, 45}
s.add(1)
s.add(12.3)
s.add(2+4j)
s.add()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s
{1, 2, 3, 6, 7, 12.3, (2+4j), 89, 45}
s={1,1,1,1,1,1,}
s
{1}
l={10,20,30}
m={1,2,3,4,}
l+m
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
s
{1}
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
#union
a|b
{1, 2, 3, 4, 5, 7, 9}
#intersection
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
{1}<=a
True
{1,2,3,4,}<=a
True
a
{1, 2, 3, 4, 5}
{1,2,3,4,5}<=a
True
a.isdisjoint ({9,10}

a.union(b)
              
SyntaxError: '(' was never closed
a.union(b)
              
{1, 2, 3, 4, 5, 7, 9}
a.subset(b)
              
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.subset(b)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
a.superset(b)
              
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
a.issuperset(b)
              
False
a
              
{1, 2, 3, 4, 5}
4 in a
              
True
8 in a
              
False
#set methods
              
max(a)
              
5
min(a)
              
1
sorted(a)
              
[1, 2, 3, 4, 5]
sum(a)
              
15
b=a
              
b
              
{1, 2, 3, 4, 5}
b
              
{1, 2, 3, 4, 5}
b.add(12)
              
b
              
{1, 2, 3, 4, 5, 12}
a
              
{1, 2, 3, 4, 5, 12}
c=a.copy()
              
c=add(13)
              
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c=add(13)
NameError: name 'add' is not defined
c=a.copy()
              
c=a.copy()
              
c=a.copy()
              
c.add()
              
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    c.add()
TypeError: set.add() takes exactly one argument (0 given)
a
              
{1, 2, 3, 4, 5, 12}
c = a.copy()
              
c.add(12)
              
c.add(13)
              
c
              
{1, 2, 3, 4, 5, 12, 13}
a
              
{1, 2, 3, 4, 5, 12}
a.add(123)
              
a
              
{1, 2, 3, 4, 5, 123, 12}
a.update({16,17,12})
              
a
              
{1, 2, 3, 4, 5, 12, 16, 17, 123}
a.pop()
              
1
a.pop()
              
2
a
              
{3, 4, 5, 12, 16, 17, 123}
a.remove(17)
              
a
              
{3, 4, 5, 12, 16, 123}
a.remove(3)
              
a
              
{4, 5, 12, 16, 123}
len(10)
              
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    len(10)
TypeError: object of type 'int' has no len()
len(a)
              
5
any(a)
              
True
a=frozenset({1,12,13,10,18,59,20})
              
a
              
frozenset({1, 18, 20, 10, 59, 12, 13})
a.add(12)
              
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
#dic
              
#dictionary
              
d={}
              
d=dic()
              
Traceback (most recent call last):

  File "<pyshell#89>", line 1, in <module>
    d=dic()
NameError: name 'dic' is not defined. Did you mean: 'dir'?
d=dict()
              
type(d)
              
<class 'dict'>
d={'k1':'v1','k2':'v2'}
              
d
              
{'k1': 'v1', 'k2': 'v2'}
id(d)
              
2458233164800
d['k4']='v4'
              
d
              
{'k1': 'v1', 'k2': 'v2', 'k4': 'v4'}
d={}
              
d[1]='int'
              
d
              
{1: 'int'}
d[12.3]='flt'
              
d
              
{1: 'int', 12.3: 'flt'}
d[2+3j]='com'
              
d
              
{1: 'int', 12.3: 'flt', (2+3j): 'com'}
d['str']='string'
              
d
              
{1: 'int', 12.3: 'flt', (2+3j): 'com', 'str': 'string'}
d[(1,2,3,4)]='tuple'
              
d
              
{1: 'int', 12.3: 'flt', (2+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d
              
{1: 'int', 12.3: 'flt', (2+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d={}
              
d[1]=1
              
d[2]=12.5
              
d[3]=12+3j
              
d[4]='str'
              
d[5]=[4,5,5,6,]
              
d[6]=(2,5,6)
              
d[7]={1,2,3,}
              
d[8]={1:1}
              
d[9]=True
              
d
              
{1: 1, 2: 12.5, 3: (12+3j), 4: 'str', 5: [4, 5, 5, 6], 6: (2, 5, 6), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
9 in d
              
True
10 in d
              
False
'str in d
              
SyntaxError: unterminated string literal (detected at line 1)
'str' in d
...               
False
>>> d[4]
...               
'str'
>>> d[5]
...               
[4, 5, 5, 6]
>>> d[8]
...               
{1: 1}
>>> get.get(10)
...               
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    get.get(10)
NameError: name 'get' is not defined. Did you mean: 'set'?
>>> d.get(1)
...               
1
>>> d.get(10,"key is not present
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> '
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> d.get(10,"key is not present")
...       
'key is not present'
>>> d.get(6,"key is not prsent")
...       
(2, 5, 6)
>>> d
...       
{1: 1, 2: 12.5, 3: (12+3j), 4: 'str', 5: [4, 5, 5, 6], 6: (2, 5, 6), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=4
...       
>>> d
...       
{1: 1, 2: 12.5, 3: 4, 4: 'str', 5: [4, 5, 5, 6], 6: (2, 5, 6), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
