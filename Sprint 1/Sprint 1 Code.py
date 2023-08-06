
menu_answers = ['1', '2', '3', '4', '5']  # accepted inputs for main menu


def main_menu():
    """
    Prints the main menu
    """

    menu_icons = ["️️1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]

    menu_items = ["Start New Simulation",
                  "View Motion Graph and Data",
                  "Export Simulation Data",
                  "Help",
                  "Exit"]

    print()
    print("–" * 36)
    print(" 🚀 Projectile Motion Simulation 📈")
    print("–" * 36)

    # loop iterates through menu icons and answers list to display main menu
    for i in range(5):
        print(menu_icons[i], menu_items[i])

    print("–" * 36)


def help():
    """
    Displays the help menu, explaining the program
    and the physics behind the simulation
    https://blog.finxter.com/how-to-print-the-content-of-a-txt-file-in-python/
    """

    # opening the help file and displaying the content
    help_file = open("../help.txt")
    help_content = help_file.read()
    print(help_content)


run_code = True

# running code as long as run_code = True
while run_code:

    main_menu()  # displaying the menu
    menu_input = input("➡️ Enter a choice: ").strip()

    # if input is 1, calls function to start new simulation
    if menu_input == "1":
        print()

    # if input is 2, calls function to display motion graph and data
    elif menu_input == "2":
        print()

    # if input is 3, calls function to export motion data as file
    elif menu_input == "3":
        print()

    # if input is 4, displays the help menu, explaining the simulation
    elif menu_input == "4":
        help()

    # if input is 5, sets run_code to False, terminating the program
    elif menu_input == "5":
        print("\nThank you for using the Projectile Motion Simulation.")
        run_code = False

    #
    else:
        print("    ⚠️ Sorry that is not a valid choice!")
