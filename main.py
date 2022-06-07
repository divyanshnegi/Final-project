import admin
from user import User

uhh = User(str, str, str, str, str)

inp = int(input("\nWhere You want to login select 1.Admin and 2.User and 3.Exit\n"))
if inp == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if admin.admin_credentials[Username] == Password:
        print("*****You're successfully logged inn*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("\nChoose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW ORIGINAL INVENTORY "
                                   "4.VIEW UPDATED INVENTORY 5.REMOVE ITEM 6.EXIT\n"))
            if adm_choice == 1:
                admin.add_new_item()
            elif adm_choice == 2:
                admin.edit_from_item()
            elif adm_choice == 3:
                admin.show_inventory()
            elif adm_choice == 4:
                admin.updated_inventory()
            elif adm_choice == 5:
                admin.remove_item()
            elif adm_choice == 6:
                print(f"You're Exit to the admin panel{Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
elif inp == 2:
    print("Welcome to the user panel. Now enter the required details that will be asked to register into the user account")
    uhh = User(input("name :"), input("enter phone number :"), input("email address:"), input("address :"), input("password :"))
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
        print(f"You are logged in successfully {username}")
        user_crawler = True
        while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history 3.Update profile 4.Exit:\t"))
            if usr_choice == 1:
                uhh.place_order()
            elif usr_choice == 2:
                print(f"Here is your order history, {username}")
                print(uhh.order_history)
            elif usr_choice == 3:
                uhh.profile_register()
            elif usr_choice == 4:
                user_crawler = False
                print("You're Successfully logged out")
            else:
                print("You Enter the invalid choice" + "\t" "PLEASE TRY AGAIN")
    else:
        print("These are the wrong credentials! SORRY!!!")
else:
    exit()
