from menu import *

x = 0
br = BadgeRepo()
doors = {}

while x == 0:
    print("Welcome Komodo Security Admin!\n")
    user_input = input("What you would like to do today?: \n"
                       "1) Add a new badge\n"
                       "2) View all created badges\n"
                       "3) Update a badge\n"
                       "4) Exit\n"
                       "> ")
    print("\n")
    if user_input == "1":
        badgeid = input("What is the badge id of the new badge?: ")
        door1 = input(
            "What door(s) would you like this badge to have access to?: ")
        doors.update({badgeid: door1})
        door_list = []
        door_list.append(door1)
        while True:
            yes_or_no = input(
                "Add a different door(s)? (yes or no): ").lower()
            if yes_or_no == "yes":
                andoor = input(
                    "What is a different door you would like this badge to have access to?: ")
                door_list.append(andoor)
                doors.update({badgeid: door_list})
            elif yes_or_no == "no":
                br.create_badge(badgeid, door_list)
                break
            else:
                print("Invalid input, please try again.")
        print("New badge added to the database.")
    elif user_input == "2":
        br.view_badges()
    elif user_input == "3":
        ex = (input("What badge would you like to update? "))
        new_door = input(
            "Please list all of the door(s) would you like the this badge to have access to: ")
        if (ex) == badgeid:
            badges.update({str(ex): [new_door]})
            print("Badge successfully updated!")
        else:
            continue

    elif user_input == "4":
        exit()
    else:
        print("invalid input")
        pass

# It's hacky, but it meets the MVP requirements. There needs to be more and better error catching, and maybe a different menu for the admin to make additional updates to the badges.
