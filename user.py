import admin as ad


class User:
    username = " "
    password = " "
    login_info = {"username": username, "password": password}

    def __init__(self, full_name, phone_no, email, address, password):
        self.name = full_name
        self.number = phone_no
        self.email = email
        self.address = address
        self.password = password
        User.login_info["username"] = full_name
        User.login_info["password"] = password
        self.profile = {"Name": full_name}
        self.order_history = {}

    @classmethod
    def login(cls, full_name, password):
        if cls.login_info["username"] == full_name and cls.login_info["password"] == password:
            print("You're are successfully logged in.....")
            return True
        else:
            print("SORRY! These are the Wrong Credentials")
            return False

    def place_order(self):
        print("<---What you want to place order--->")
        print(ad.updated_inventory())
        user_choice = int(input("\nIf you want to order then select 1.YES 2.NO:\t"))
        if user_choice == 1:
            print(ad.updated_inventory())
            n = int(input("Enter how many items do you want to Order:\t"))
            x = 0
            z = 0
            for i in range(n):
                itemid = int(input("Enter the Item id here: "))
                print("Please enter equal or more than the quantity of the items.")
                quant = int(input("Enter the quantity of the item: "))
                cost = ad.final_cost(itemid)
                quantity = int(ad.inventory[itemid]["Quantity"])
                if quant >= quantity:
                    x = x + ((cost * quant) / quantity)
                confirm_order = input("\nAre you sure to buy this order YES or NO:")
                if confirm_order == "YES" or confirm_order == "yes":
                    # user could enter in uppercase and lowercase
                    print(f'''Your item name is {ad.inventory[itemid]["ItemName"]}''')
                    print(f'''Price of your Item is {ad.inventory[itemid]["Price"]}''')
                    print(f"This is your quantity {quant}")
                    print(f"It costs you {x}INR in total")
                    print("You're all set for this order")
                    z = z + x
                    self.order_history[itemid] = {
                        "Item Name": ad.inventory[itemid]["ItemName"],
                        "Price": ad.inventory[itemid]["Price"],
                        "Quantity": quant
                    }
                    w = quant/quantity
                    final_stock = ad.inventory[itemid]["Stock"] - w
                    ad.inventory[itemid]["Stock"] = final_stock
                    print("The stock left for this item is:", ad.inventory[itemid]["Stock"])
                    print("Your final amount to pay is =", z)
                    print("You're order is successfully placed")

                elif confirm_order == "NO" or confirm_order == "no":
                    print("This Order is cancelled!! You can look once more")
                else:
                    print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("You Enter the invalid choice" + "\t" "PLEASE TRY AGAIN")

    def update_login(self):
        if self.login_info["username"] == self.name and self.login_info["password"] == self.password:
            print("Your profile is updated and You're are successfully logged in.....")
            print("#####YOUR UPDATED PROFILE DETAILS:#####")
            print("Updated name:", self.name)
            print("Updated number:", self.number)
            print("Updated email:", self.email)
            print("Updated address:", self.address)
            print("Updated password:", self.password)
            print("Updated login_info:", User.login_info)
        else:
            print("SORRY! These are the Wrong Credentials")
            return False

    def profile_update(self):
        update = User(input("Enter name: "), int(input("Enter number: ")), input("Enter email_id: "), input("Enter address: "),
                      input("Enter password: "))
        return update.update_login()

    def profile_register(self):
        print("#####YOUR PROFILE DETAILS:#####")
        print("please enter name:", self.name)
        print("enter number:", self.number)
        print("enter email:", self.email)
        print("enter address:", self.address)
        print("please enter password:", self.password)
        print("enter your login_info:", User.login_info)
        return self.profile_update()
