# 1. Print numbers 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1


# 2. Print numbers 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1


# 3. Print even numbers from 2 to 100
i = 2
while i <= 100:
    print(i, end=' ')
    i += 2

print()


# 4. Reverse a string
s = "Python Programming"
i = len(s) - 1

while i >= 0:
    print(s[i], end='')
    i -= 1

print()


# 5. Remove all zeros from list
l = [1, 0, 0, 0, 2, 3, 4, 5, 56, 12, 0, 12, 0, 13, 0, 0, 0, 16, 0]

while 0 in l:
    l.remove(0)

print(l)


# 6. Product bill
d = {}
total_bill = 0

while True:
    product = input("Enter product name (for exit): ")

    if product == "exit":
        break

    price = float(input("Enter product price: "))
    total_bill += price
    d[product] = price

print(d)
print("Total Bill:", total_bill)


# 7. While loop with break and else
i = 0

while i < 20:
    i += 1

    if i == 15:
        break

    print(i, end=' ')
else:
    print("End of the loop")