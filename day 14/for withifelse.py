'''for i in range(1,18):
    if i==15:
        break
    print(i)
else:
    print("End of the loop")
    
pin=1234
for _ in range(5):
    epin=int(input("Enter your pin: "))
    if epin==pin:
        print("Unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try again after 30 seconds")
    
n=int(input("Enter a number: "))
print("factors :",end=' ')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
        
n=int(input("Enter a number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime number")
else:
    print("Not a prime number")'''
    
    
n=int(input("Enter a number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")