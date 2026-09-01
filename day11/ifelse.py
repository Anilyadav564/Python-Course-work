username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "admin"
    print("Login Successful")
else:
    print("Invalid Credentials")

# Product Search
products = ["laptop", "mobile", "watch"]

search = input("Search Product: ")

if search.lower() in products:
    print("Product Found")
else:
    print("Product Not Found")

# Bill Calculation
bill = int(input("Enter the Bill Amount: "))

if bill > 99:
    print("Final Bill:", bill)
else:
    print("Final Bill:", bill + 30)
    
    