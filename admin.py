admin_credentials = {"Divyansh": "divyansh1996", "Sarthak": "sarthak1992", "Arti": "arti1990"}
# With these credential login is possible.
r = [3, 4, 5, 6, 7, 9, 13]
s = [1, 2, 8, 10, 11, 12]
inventory = {1: {'ItemName': 'Mushroom Sandwich', 'ItemID': 1, 'Price': 30, 'Quantity': 4, 'Stock': 110, 'Discount': 5},
             2: {'ItemName': 'Pizza', 'ItemID': 2, 'Price': 220, 'Quantity': 1, 'Stock': 150, 'Discount': 6},
             3: {'ItemName': 'Fried Rice', 'ItemID': 3, 'Price': 50, 'Quantity': 250, 'Stock': 180, 'Discount': 5},
             4: {'ItemName': 'Black Forest Cake', 'ItemID': 4, 'Price': 250, 'Quantity': 500, 'Stock': 110, 'Discount': 10},
             5: {'ItemName': 'Butterscotch Pineapple Cake', 'ItemID': 5, 'Price': 200, 'Quantity': 450, 'Stock': 90,
                 'Discount': 10},
             6: {'ItemName': 'Honey Chile Potato', 'ItemID': 6, 'Price': 80, 'Quantity': 300, 'Stock': 200, 'Discount': 6},
             7: {'ItemName': 'Peri Peri Pasta', 'ItemID': 7, 'Price': 130, 'Quantity': 300, 'Stock': 150, 'Discount': 7},
             8: {'ItemName': 'Cheese Momos', 'ItemID': 8, 'Price': 70, 'Quantity': 8, 'Stock': 250, 'Discount': 4},
             9: {'ItemName': 'Veg. Manchurian', 'ItemID': 9, 'Price': 40, 'Quantity': 200, 'Stock': 190, 'Discount': 8},
             10: {'ItemName': 'Kathi roll', 'ItemID': 10, 'Price': 60, 'Quantity': 1, 'Stock': 300, 'Discount': 9},
             11: {'ItemName': 'Tandoori Chicken', 'ItemID': 11, 'Quantity': 5, 'Price': 240, 'Stock': 110, 'Discount': 11},
             12: {'ItemName': 'Vegan Burger', 'ItemID': 12, 'Quantity': 1, 'Price': 320, 'Stock': 120, 'Discount': 9},
             13: {'ItemName': 'Truffle Cake', 'ItemID': 13, 'Quantity': 400, 'Price': 900, 'Stock': 70, 'Discount': 10}
             }


# nested dictionary of 13 food items in it.

def qty_weight(x):
    print("Item Name: ", inventory[x]["ItemName"])
    print("Item ID: ", inventory[x]["ItemID"])
    print("Quantity: ", inventory[x]["Quantity"], "grams")
    print("Price: ", inventory[x]["Price"], "INR")
    print("Stock: ", inventory[x]["Stock"])
    print("Discount: ", inventory[x]["Discount"], "%")


def qty_pieces(y):
    print("Item Name: ", inventory[y]["ItemName"])
    print("Item ID: ", inventory[y]["ItemID"])
    print("Quantity: ", inventory[y]["Quantity"], "pieces")
    print("Price: ", inventory[y]["Price"], "INR")
    print("Stock: ", inventory[y]["Stock"])
    print("Discount: ", inventory[y]["Discount"], "%")


def add_new_item():
    global r
    global s
    print("Guidelines:-1. Please follow to enter the sequential order of itemid,2.Since, you have come this far there is no exit "
          "from here so, please do not input any invalid options or you could get struct in infinite loop in some part of codes")
    m = int(input('Enter: 1 for entering quantity in grams 2 for entering quantity in pieces and 3 for entering in both\n'))
    n = [1, 2, 3]
    while m not in n:
        print('!!!Again!!!\tPlease do not enter any invalid input because u could struct in infinite loop of entering inputs')
        m = int(input())
    if m == 1 or m == 3:
        print("You entered into gram list")
        itemname = input("Enter the Item name: ")
        itemid = int(input("Enter the item id: "))
        price = int(input("Enter the price of the item: "))
        stock = int(input("Enter the stock value of item: "))
        quantity = int(input("enter quantity:"))
        discount = int(input("enter discount:"))
        inventory[itemid] = {
            "ItemName": itemname,
            "ItemID": itemid,
            "Quantity": quantity,
            "Price": price,
            "Stock": stock,
            "Discount": discount
        }
        r.append(itemid)
        print("The Item\t" + itemname + "\tis successfully added")
        print('The available itemids in gram list:', r)
        print("Total count of available items in inventory is:-%d" % len(inventory))

    if m == 2 or m == 3:
        print("You entered into piece list")
        itemname = input("Enter the Item name: ")
        itemid = int(input("Enter the item id: "))
        price = int(input("Enter the price of the item: "))
        stock = int(input("Enter the stock value of item: "))
        quantity = int(input("enter quantity:"))
        discount = int(input("enter discount:"))
        inventory[itemid] = {
            "ItemName": itemname,
            "ItemID": itemid,
            "Quantity": quantity,
            "Price": price,
            "Stock": stock,
            "Discount": discount
        }
        s.append(itemid)
        print("The Item\t" + itemname + "\tis successfully added")
        print('The available itemids in piece list:', s)
        print("Total count of available items in inventory is:-%d" % len(inventory))
    print(inventory)


def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the quantity of item"))
    c = int(input("Enter the price of item"))
    d = int(input("Enter the stock of the item"))
    e = int(input("Enter the discount of item"))
    inventory[item]["ItemName"] = a
    inventory[item]["quantity"] = b
    inventory[item]["price"] = c
    inventory[item]["stock"] = d
    inventory[item]["discount"] = e
    print("*****Edited item successfully*****")
    return inventory


def show_inventory():
    # The original inventory with no updated items.
    print("*****HERE IS THE INVENTORY OF Items*****")
    gram = [3, 4, 5, 6, 7, 9, 13]
    for i in gram:
        qty_weight(i)
    piece = [1, 2, 8, 10, 11, 12]
    for i in piece:
        qty_pieces(i)


def updated_inventory():
    # Updated inventory with updated items.
    print('The Inventory could looks same as original if nothing is updated')
    for i in r:
        qty_weight(i)
    for i in s:
        qty_pieces(i)


def final_cost(item):
    # final cost after discount is added.
    a = inventory[item]["Price"]
    dis = inventory[item]["Discount"]
    total = a - ((a * dis) / 100)
    return total


def remove_item():
    print("Guideline:-If you enter to remove the original itemsid of inventory dictionary then u will not be able to see the results "
          "of the show_inventory function.So,If you choose to do it then please do not choose to see the view original items because "
          "that will be a insignificant choice of yours")
    d = int(input("Enter the Item id which you want to vanish:-"))
    inventory.pop(d)
    if d in r:
        r.remove(d)
    elif d in s:
        s.remove(d)
    else:
        pass
    print("Item removed successfully ")
    print(inventory)
