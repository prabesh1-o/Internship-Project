menu ={
    'Pizza':150,
    'Pasta':50,
    'Salad':100,
    'Coffee':60,
    'Burger':90
}

print("Welcome to Turning Cafe")
print("Pizza :Rs.150\nPaste:Rs.50\nSalad:Rs.10\nCoffee:Rs.60\nBurger:Rs.90")

order_total = 0
item = input("enter the item you want to have :")
if item in menu:
    order_total = menu[item]
    print(f"Your {item} has been sucessfully added to your order.")
else:
    print('Please order something else we can serve you')

another_order = input("Do you want to add another item(Yes/No)")
if another_order=='Yes':
    item2 = input("enter the another item")
    if item2 in menu:
        order_total = menu[item2]
        print(f"Your {item2} has added")
    else:
        print('Please order something else we can serve you')
print(f"The total amount is to be paid is {order_total}")