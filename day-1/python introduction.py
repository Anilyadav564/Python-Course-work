# Print Name
name = "Anil"
print(name)

# Procedural Programming
def login():
    print("Login")

def select_restaurant():
    print("Select restaurant")

def select_food():
    print("Select food")

def payment():
    print("Payment")

def confirm_order():
    print("Order confirmation")

login()
select_restaurant()
select_food()
payment()
confirm_order()

# Variables
name = "Ravi"
price = 500

print(name)
print(price)
#oops
#object from real life
#ex
class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def show_details(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Rating:", self.rating)

    def buy_now(self):
        print(self.name, "bought successfully")

product1 = Product("Laptop", 50000, 4.5)

product1.show_details()
product1.buy_now()


