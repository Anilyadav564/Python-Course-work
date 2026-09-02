'''s= 'python programing'
for i in range(len(s)):
    if s[i]in 'aeiouAEIOU':
        print(i,s[i])'''
''' l=[23,45,12,34,50,24,35,68,75,34,10]
sum=0
for i in range(len(l)):
if l[i]%2==0:
    sum=sum+i
    print(i,l[i]
    print(sum)
    '''
'''num = int (input("enter a number:"))
fact = 1
for i  in range (1, num + 1):
    fact = fact *i
    print("factorial=", fact)''' ``
'''n= int(input("enter the no of students:"))
max_marks=0
for i in range(n):
   name= input("enter the name:")
   marks = int(input("enter the marks:"))
   if marks > max_marks:
     max_marks = marks
     data[name] = marks
     print(data)
     print("maximum marks:",max_marks)
     
 '''

n=int(input("enter the no of  products:"))
total_bill = 0
products = {}
for i in range(n):
    products = input(f"product-{i}:")
    price= float(input(f"price-{i}:"))
    quantity= int(input(f"quantity-{i}:"))
    final_price= price*quantity
    total_bill +=final_price
    products[products]= f'{price} *{quamtity} = {final_price}'
    print(products)
    print("total bill:",total_bill)
    


    
        
        



    