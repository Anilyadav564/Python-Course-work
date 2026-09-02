'''def display(n):
    n=n+10#local variable 
    print('Inside:',n)
n=10#global variable
display(n)
print('outside:',n)'''
#here only pass globalit effects local aslo
'''def display(n):
    #local variable 
    print('Inside:',n)
n=10#global variable
display(n)
print('outside:',n)'''
#here only local declared variable it not effect global var
'''def display():
    n=10#local variable 
    print('Inside:',n)
#global variable
display()
print('outside:',n)'''
#ex more clear
'''def display():
    global n
    n='pfs'
    print("updated course:",n)
n='jfs'
display()
print("final course:",n)'''
#ex
def display(n):
    n='pfs'
    print("updated course:",n)
n='jfs'
display(n)
print("final course:",n)
#ex nested nonlocal 
def display():
    n='jfs'
    def update():
        nonlocal n
        n='pfs'
        print("updated course:",n)
    update()
    print("final course:",n)
    