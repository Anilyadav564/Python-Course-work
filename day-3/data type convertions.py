Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Data type convertions
>>> #int convertions
>>> a = 10
>>> float(a)
10.0
>>> str(a)
'10'
>>> complex(a)
(10+0j)
>>> bool(a)
True
>>> #float convertions
>>> a = 10.2
>>> int(a)
10
>>> complex(a)
(10.2+0j)
>>> str(a)
'10.2'
>>> bool(a)
True
>>> #str convertions
>>> s =  "Anil"
>>> list(s)
['A', 'n', 'i', 'l']
>>> set(s)
{'i', 'l', 'A', 'n'}
>>> tuple(s)
('A', 'n', 'i', 'l')
>>> bool(s)
True
>>> #list convertions
>>> l = [1,2,3,4,5]
>>> bool(l)
True
>>> str(l)
'[1, 2, 3, 4, 5]'
>>> tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
#tuple convertions
t =  (1,2,3,4,5)
str(t)
'(1, 2, 3, 4, 5)'
list(t)
[1, 2, 3, 4, 5]
set(l)
{1, 2, 3, 4, 5}
bool(t)
True
#set convertions
s = {1,2,3,4,5}
str(s)
'{1, 2, 3, 4, 5}'
list(s)
[1, 2, 3, 4, 5]
tuple(s)
(1, 2, 3, 4, 5)
bool(s)
True
#dictionary convertions
d = {1:2,2:4,3:6}
str(d)
'{1: 2, 2: 4, 3: 6}'
list(d)
[1, 2, 3]
tuple(d)
(1, 2, 3)
set(d)
{1, 2, 3}
bool(d)
True
#boolean convertions
b = true
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b = true
NameError: name 'true' is not defined. Did you mean: 'True'?
b = True
int(b)
1
float(b)
1.0
str(b)
'True'
complex(d)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
complex(b)
(1+0j)
