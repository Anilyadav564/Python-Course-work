#immportant point
#display()
'''l=[1,2,34,5,]
max=20
sum=10
print(sum(l))'''
#by using summ max as a variable so sum losss it property
'''l=[1,2,34,5,]
max=20
sum=10
print(sum)'''
#use like this
#ex call by value
#int,float str tuple bool- immutable (pass by value)(1)
#list set dict mutable -(pass by reference)(2)
#ex(2)
def display(n):
    n[5]=6
    print('inside:',n)
n={1:2,3:4}
display(n)
print('outside:',n)
