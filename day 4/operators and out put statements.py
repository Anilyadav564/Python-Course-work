Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
a**3
8000
a**b
10240000000000
a=20
b=10
a<b
False
a>b
True
a<=b
False

a>=b
True
a!=b
True
a=b

a==b
True
a!==b
SyntaxError: invalid syntax
c=10+30
c
40
c+=10
c
50
c-=10
c
40
c*=2
c
80
c//=2
c
40
c**=2
c
1600
c%=3
c
1
c/=2
c
0.5
true and false
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    true and false
NameError: name 'true' is not defined. Did you mean: 'True'?
true or false
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    true or false
NameError: name 'true' is not defined. Did you mean: 'True'?
n=10
n%2==0
True
n%2==0 and n%3==0
False
n%2==0 or n%4==0
True
n
10
n<5
False
not n<5
True
#str list tuple set dict
s='anilyadav'
'a'in s
True
'p'in s
False
l={1,2,3,4,5,9}
'1' in l
False
'9'in l
False
l=[1,2,3,4,5,6,]
'1'in l
False
1 in l
True
#tuple
t=(1,2,3,4,5,6)
4 in t
True
d={'name':'anil','batch':63,'course':'python'}
'name'in d
True
'anil'in d
False
63 in d
False
'python'in d
False
'batch;in d
SyntaxError: unterminated string literal (detected at line 1)
'batch'in d
True
'course'in d
True
#identity operator
l=[1,2,3,4]
m=[1,2,3,4,]
id(1)
140726839739304
id(l)
2999112115072
id(m)
2999112115328
l is m
False
n=l
id(n)
2999112115072
l is n
True
#mutable and imutable
a=20
a
20
id(a)
140726839739912
s={1,2,3,4}
id(s)
2999111832000
is(a)
SyntaxError: invalid syntax
id(a)
140726839739912
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
2999111832000
9&10
8
bitwise operators
SyntaxError: invalid syntax
9&10
8
9|10
11
9^10
3
8>>2
2
8<<2
32
8>>3
1
~8
-9
~12
-13
~45
-46
#COMMA separation
a=10
b=10.3
c='anilyadav'
print(a,b,c)
10 10.3 anilyadav
print("a value is ",a)
a value is  10
>>> print("a value is",a,"|b value is ",b,'|c value is ',c)
a value is 10 |b value is  10.3 |c value is  anilyadav
>>> print(a,b,c)
10 10.3 anilyadav
>>> print(a,b,c,sep='')
1010.3anilyadav
>>> print(a,b,c,sep='\n')
10
10.3
anilyadav
>>> print(a,b,c,sep='\t')
10	10.3	anilyadav
>>> printI(a,b,c,sep '\t',end='@')
SyntaxError: invalid syntax
>>> rintI(a,b,c,sep ='\t',end='@')
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    rintI(a,b,c,sep ='\t',end='@')
NameError: name 'rintI' is not defined. Did you mean: 'print'?
>>> printI(a,b,c,sep= '\t',end='@')
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    printI(a,b,c,sep= '\t',end='@')
NameError: name 'printI' is not defined. Did you mean: 'print'?
>>> print(a,b,c,sep = '\t',end='@')
10	10.3	anilyadav@
>>> print(a,b,c,sep='\t',end='\n\n')
10	10.3	anilyadav

>>> #recummended best is
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.3 c=anilyadav
>>> #and aslo do
>>> print(f"avalue is {a} | b value is {b} | c value is {c}")
avalue is 10 | b value is 10.3 | c value is anilyadav
>>> print('a=%d b= %f c=%s'%(a,b,c))
a=10 b= 10.300000 c=anilyadav
>>> print('a=%d b= %.2f c=%s'%(a,b,c))
a=10 b= 10.30 c=anilyadav
