#print 1to 10 using recursive
'''def display(n):
    if n<10:
        return
    print(n)
    display(n+1)
display(1)'''
#now printing 10 to 1
'''def display(n):
    if n<10:
        return
    display(n+1)
    print(n)
display(1)'''
#printing sum of numbers
'''def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)
print(displaysum(8))'''
#product printing

def productofn(n):
    if n==1:
        return 1
    return n*productofn(n-1)
print(productofn(5))
#printing index reverse
'''def display(ind):
    if ind ==len(s):
        return
    display(ind+1)
    print(s[ind],end='')
s= 'python programming'
display(0)'''
#This program prints the string one character at a time growing from left to right.
'''def display(n):
    if n>len(s):
        return
    print(s[:n])
    display(n+1)
s='python programming'
display(1)'''
#Print consecutive 3-letter groups from a string using recursion."

'''def display(i):
    if i ==len(s):
        return
    print(s[i:i+3])
    display(i+1)
s="python"
display(0)'''
#"Printing String Characters and Number Digits Using Recursion".
def display(n):
    if n==0:
        return
    display(n//10)
    print(n%10)
n=987654
display(n)
#fibonacci Series Using Function (Recursion)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i), end=" ")

        

        