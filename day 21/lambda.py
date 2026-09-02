'''Easy Exam Definition

Lambda Function: A lambda function is an anonymous (nameless) function used for short, 
simple operations'''
'''def  → Big function with name

lambda → Small function without name'''
'''grater = lambda a,b: a if a>b else b
print(grater(10,30))
print(grater(20,10))
greater = lambda a,b: a if a>b else b
print(greater(13,16))
print(greater(60,46))
print(greater(34,27))
print(greater(50,30))
#wishing
wish = lambda name: f'Welcome to the course {name}'
print(wish("Ganesh"))
print(wish("Viswa"))
print(wish("Cherry"))
#even or add
iseven = lambda n: "Even" if n%2==0 else "Odd"
print(iseven(67))
print(iseven(80))
print(iseven(78))
#average of
avg = lambda a,b,c: (a+b+c)/3
print(avg(4,5,6))
print(avg(45,68,17))
#spliting gmail
domain = lambda mail:(mail.split('@')[-1]).split('.')[0]
print(domain('Anil@codegnan.com'))
print(domain("anil@gmail.com"))
#printing price
gst = lambda price : price+price*0.18
print(gst(1000))
print(gst(5000))
print(gst(3000))'''
#using map
'''price = [5678,8765,5467,124,1600,3000]
res = list(map(lambda price : price+price*0.18,price))
print(res)
#coverting into title
names =['anil','ganesh','avinash']
res = list(map(lambda name :name.title(),names))#list is ued to covert object refernce to list
print(res)
#30% discount
prices = [1000,2000,3000,4000]
res =   list( map( lambda price: price - price*0.3,price))#map used for update
print(res)
#filtering using filter only some values
price = [1000,5000,6000,8000]
res =    list(filter(lambda price : price>5000,price))
print(res)
#even or odd
price = [1000,5000,6000,8000]
res =    list(filter(lambda price : price %2==0,price))
print(res)'''
#filtering names from list
'''names = ['anil','ganesh']
'''
#sum of elements
from functools import reduce
l= [30,56,60,20]
res = reduce(lambda sum,i:sum+i,l)
print(res)
names = ['anil','ganesh','avinash']
res =     reduce(lambda res,i:res+' '+i,names)
print(res)
#tuple of dictionary
products = {'sugar':60,
            'salt' :50,
            'eggs' :90,
            'cooking oil':120,
            'bread' : 45
            } 
print(dict(sorted(products.item())))
print(dict(sorted(products.items(),reverse=True)))
print(dict(sorted(products.item(),key = lambda i:i[1])))
print(dict(sorted(products.item(),key = lambda i:i[1],reverse = True)))

