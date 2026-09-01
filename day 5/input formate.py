Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x= input()
anilyadav
x
'anilyadav'
# that is input of string get
age = input("enter the age :")
enter the age :21
age
'21'
#now
age = int (input("enter the age :"))
enter the age :21
age
21
#from str out to get input integer
>>> names = input("enter the names :")
enter the names :anil avinash ganesh
>>> names
'anil avinash ganesh'
>>> names .split()
['anil', 'avinash', 'ganesh']
>>> # we get list
>>> names = input("enter the names :").split()
enter the names : 1 2 3 4 5 56
>>> names
['1', '2', '3', '4', '5', '56']
>>> #we got list of str
>>> map (int,names )
<map object at 0x00000271BC513130>
>>> list (map(int,names))
[1, 2, 3, 4, 5, 56]
>>> values = list (map(int,input().split()))
1 2  3 4 5 56
>>> values
[1, 2, 3, 4, 5, 56]
>>> names = tuples ( input("enter  the names :").split())
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names = tuples ( input("enter  the names :").split())
NameError: name 'tuples' is not defined. Did you mean: 'tuple'?
>>> names = input("enter the names :").split())
SyntaxError: unmatched ')'
>>> values [2.0,3.5.456.345.56]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> alues [2.0,3.5,567.7]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    alues [2.0,3.5,567.7]
NameError: name 'alues' is not defined. Did you mean: 'values'?
>>> KeyboardInterrupt
>>> values =[2.3,5.6.7.8]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> values =[2.3,5.6,]
>>> names = set (map (int,input ().split()))
1 2 3 4 
>>> a,b=[1,2]
a
1
b
2
a,b
(1, 2)
a
1
b
2
email,password= input ("enter the email and  password:").split())
SyntaxError: unmatched ')'
email,password= input ("enter the email and  password:").split()
enter the email and  password:123444555
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    email,password= input ("enter the email and  password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password= input ("enter the email and  password:").split()
enter the email and  password:anilyadav@8404.com
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    email,password= input ("enter the email and  password:").split()
ValueError: not enough values to unpack (expected 2, got 1)

email,password= input ("enter the email and  password:").split()
enter the email and  password:sowmya@codegnan.com 123345
email
'sowmya@codegnan.com'
password
'123345'
a,b,c =list (map(int input().split())
             
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a,b,c =list (map(int, input().split())
             a,b,c =list (map(intinput().split())
                          
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a,b,c =list(map(int,input().split())
 a
            
SyntaxError: '(' was never closed
a,b,c =list(map(int,input().split()))
            
email,password= input ("enter the email and  password:").split()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a,b,c =list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'email,password='
 e = eval (input())
            
SyntaxError: unexpected indent
e=eval(input())
            
1
e
            
1
e=eval(input())
            
e=eval(input())
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    e=eval(input())
     ^
SyntaxError: invalid syntax
e= eval (input())
            

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    e= eval (input())
  File "<string>", line 0
    
SyntaxError: invalid syntax

"anil"
            
'anil'
e
            
1
