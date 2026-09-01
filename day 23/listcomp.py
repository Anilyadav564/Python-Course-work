#List comprehension means: creating a new list in one short line of Python code.
#Instead of writing a for loop and using append(), we write it shortly.
#examples
#syntax for list comp
'''
l = [updating for loop]
l = [updating for loop if cond]
l= [upd1 if cond else upd2 for loop]
l = [upd for loop1 for loop2]
l = [upd for loop1 for loop2 if cond]
res=[i for i in range(1,11)]#taking condition and updation like(i)
print(res)
n=12
#
res = [i for i in range(1,n+1) if n%i==0]
print(res)
#
r=[12,45,60,45,85]
res = [i if i%2==0 else 0 for i in r ]
print(res)
#
r=[12,23,45],[687,45,70],[34,60,80]
res =[j for i in r  for j in i if j%2==0]
print(res)'''
#set comp
'''res={i for i in range(1,11)}#taking condition and updation like(i)
print(res)
n=12
#
res = {i for i in range(1,n+1) if n%i==0}
print(res)
#
r=[12,45,60,45,85]
res = {i if i%2==0 else 0 for i in r }
print(res)'''
#

'''res=[12,23,45],[687,45,70],[34,60,80]
res ={j for i in r  for j in i if j%2==0}
print(res)'''
# comp dict using int
'''l = [int(input()) for i in range(10)]
print(l)
'''
#com of dict using int and for loop
'''names={input(f"enter the name-{i+1}:"):
        int(input("enter the marks:"))
        for i in range(5)}#here using first update and  then for loop 
print(names)'''
#dic of number and squares
s={x:x*x for x in range(1,5)}
print(s)
#store numbers and whether they are even or odd
res = {x:"even" if x%2==0 else "odd" for x in range(1,10) }
print(res)
