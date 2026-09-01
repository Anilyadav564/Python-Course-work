Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
count = 7
type(count)
<class 'int'>
price=9.9
type(price)
<class 'float'>
c=5+7k
SyntaxError: invalid decimal literal
c =  5+4j
type(c)
<class 'complex'>
c
(5+4j)
s="code"
s
'code'
type(s)
<class 'str'>
>>> l=list()
>>> l
[]
>>> type(l)
<class 'list'>
>>> L=[2,2,5,5,6,6,"anil",90.5,(2,4)]
>>> l
[]
>>> type(l)
<class 'list'>
>>> s={1,2,3,4,'23.1',23.2,'dfhn'}
>>> s
{1, 2, 3, 4, 'dfhn', 23.2, '23.1'}
>>> type(s)
<class 'set'>
>>> status= none
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    status= none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> status=None
>>> type(status)
<class 'NoneType'>
>>> s={1,2,3,4,5}
>>> s.add(6)
>>> type(s)
<class 'set'>
>>> s
{1, 2, 3, 4, 5, 6}
>>> s.remove(4)
>>> 
>>> s
{1, 2, 3, 5, 6}
>>> type(s)
<class 'set'>
>>> s=frozenset({1,2,3,4,})
>>> s
frozenset({1, 2, 3, 4})
>>> ###datatypes
>>> #type convertion
