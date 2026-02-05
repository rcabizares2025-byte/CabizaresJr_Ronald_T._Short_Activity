cart = {'apple': 2, 'banana': 5, 'milk': 1}

item = (input("Enter an item to add: "))

if item in cart:
    cart[item] += 1
else:
    cart[item] = 1

print("You have:", end=" ")

for item in cart:
    print(cart[item], item, end=", ")
