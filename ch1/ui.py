from menu import *

mr = MenuRepo()

# # mr.add_item(1, burger, hamburger, hamburger, 2): checking add_item
# mr.delete_menu_item(burger) checking delete_menu_item
# mr.view_menu() checking view_menu
# everything works as intended, plugging them into the while loop

while True:
    print("Welcome to The Komodo Cafe!")
    user_input = input("What would you like to do? (Please make a select from the numbers below) \n"
                       "1. Add a menu item \n"
                       "2. View menu \n"
                       "3. Delete a menu item \n"
                       "4. Exit \n"
                       "> ")
    print("\n")

    if user_input == "1":
        idnum = input("Enter the id number: ")
        name = input("Enter the name: ")
        desc = input("Enter a brief description of the item: ")
        ingredients = input("Enter a list of the ingredients: ")
        price = input("Enter the item's price: ")
        mr.add_item(idnum, name, desc, ingredients, price)
        print(f"added {name} has been added to the menu!")
    elif user_input == "2":
        menu = mr.view_menu()
        print(menu)
    elif user_input == "3":
        to_del = input("what menu item would you like to delete?: ")
        mr.delete_menu_item(to_del)
        print(f"{to_del} has been deleted.")
    elif user_input == "4":
        exit()
    else:
        print("Invalid input; please make a select from the numbers provided")
        pass

# Everything works as intended, but there are still some bugs that need squashed. A refactor wouldn't hurt either!
