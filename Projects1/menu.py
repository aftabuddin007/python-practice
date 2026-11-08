#Define the menu
menu={
    "A":20,
    "B":10,
    "C":40,
    "D":80,
    "E":110,
    "F":30,
    "G":50,

}
#greet
print("Welcome to the Alphabet menu")
print("Here are the available options:")
print("A:20\nB:10\nC:40\nD:80\nE:110\nF:30\nG:50")
# order total 
order_total=0
item_1=input("Please enter your first item: ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your first item {item_1} costs {menu[item_1]}")
else:
    print(f"Order item {item_1} is not available in the menu")
another_order=input("Would you like to order another item? (yes/no): ")
if another_order.lower()=="yes":
    item_2=input("Please enter your second item: ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Your second item {item_2} costs {menu[item_2]}")
    else:
        print(f"Order item {item_2} is not available in the menu")    
print(f"Your total order cost is: {order_total} to pay")
