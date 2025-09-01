# menu ={
#     'Pizza':150,
#     'Pasta':50,
#     'Salad':100,
#     'Coffee':60,
#     'Burger':90
# }

# print("Welcome to Turning Cafe")
# for item,price in menu.items():
#     print(f"{item}:RS.{price}")


# order_total = 0

# while True:
#     item = input("enter the item you want to take: ")
#     if item in menu:
#         order_total+=menu[item]
#         print(f"Your {item} has beed added")
#         print(f"The total amount to be paid is {order_total}")
#     else:
#         print("sorry we do not serve this item.please order something else")

#     another_order = input("Do you want to add another item (Yes/No)")
#     if another_order!="Yes":
#         break


# using OOP concept

class Cafe:
    def __init__(self):
        self.menu={
            'Pasta':100,
            "Milk Tea":50,
            "Milk Coffee":80,
            "Momo":150,
            "Burger":200
        }

        self.order_total = 0
        self.order_List = []

    def show_menu(self):
        print("-----Welcome to GoloCafe------------------")
        print("Menu:")
        for item,price in self.menu.items():
            print(f"{item}:Rs.{price}")

    
    def take_order(self):
        while True:
            item1 = input("Enter the item you want to order: ")
            if item1 in self.menu:
                self.order_total+=self.menu[item1]
                self.order_List.append(item1)
                print(f"Your {item1} has been added")
                

            else:
                print("sorry we do not serve this item.please order something else")

            another_order = input("Do you want to add another item (Yes/No)?")
            if another_order!='Yes':
                break

    def Show_bill(self):
        print('\n---------Show bill----------')
        for item in self.order_List:
            print(f"{item} :{self.menu[item]}")
        print(f"Total Amount to be paid: Rs.{self.order_total}")
my_cafe = Cafe()
print(my_cafe.show_menu())
print(my_cafe.take_order())
print(my_cafe.Show_bill())



