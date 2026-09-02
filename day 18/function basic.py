'''Easy Exam Definition :
#**                        **#
Function: A function is a reusable block of code that performs 
a specific task and can be called whenever needed.'''
#Reusable means: write once, use many times.
#without fuction
'''print("hello anil")
print("hellp ganesh")
print("hello avinash")
if you have 100 people you must write print()100'''
#with fuction
'''def greet(name):
    print("hello ",name)
greet("anil")#calling fuction greet
greet("ganesh")
greet("avinash")'''
#code reusable here
# Example 1: Display User details

'''def display(name,email,password):
    print('f hello{name}') 
    print('f your email{email}')
    print('f your password{password}')
display('Anil','anil@gmail.com','anil123')'''
   # Example 2: Leap Year
'''def isleapyear(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print("Leap Year")
    else:
        print("Not Leap Year")
isleapyear(2024)       
      '''
#Example 3: Sum of Digits
'''def sumofdigits(n):
    sum = 0

    while n > 0:
        sum += n % 10
        n = n // 10

    return sum

print(sumofdigits(123))'''
#Next Example:4 Product of Digits
'''def productofdigits(n):
    product = 1

    while n > 0:
        product *= n % 10
        n = n // 10

    return product

print(productofdigits(123))'''
#Example:5 Password Checker
def checkpassword(password):
    if len(password) > 0:
        check = set()

        for i in password:
            if i.isupper():
                check.add('u')
            elif i.islower():
                check.add('l')
            elif i.isdigit():
                check.add('d')
            else:
                check.add('s')

        if len(check) == 4:
            return "Strong Password"

    return "Weak Password"

password = input("Enter Password: ")
print(checkpassword(password))
