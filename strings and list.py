Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c = 'strings.py'
c = starts with ('str')
SyntaxError: invalid syntax
c.startswith('str')
True
c.endwith('py')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c.endwith('py')
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
c.ends with('py')
SyntaxError: invalid syntax
c.endswith('py')
True
c.is lower()
SyntaxError: invalid syntax
>>> c.islower()
True
>>> c.isupper()
False
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> c.isspace()
False
>>> ' 'isspace()
SyntaxError: invalid syntax
>>> ' '.isspace()
True
>>> 'this is a title'.istitle()
False
>>> this is 'Title'.istitle()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    this is 'Title'.istitle()
NameError: name 'this' is not defined. Did you forget to import 'this'?
>>> This is 'Title'.istitle()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    This is 'Title'.istitle()
NameError: name 'This' is not defined
>>> l=[]
>>> l=list[]
SyntaxError: invalid syntax
>>> l=list()
>>> l=[1,22.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},none,true]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l=[1,22.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},none,true]
NameError: name 'none' is not defined. Did you mean: 'None'?
>>>  vcxl=[1,22.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},None,True]
...  
SyntaxError: unexpected indent
>>> l=[1,22.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},None,True]
