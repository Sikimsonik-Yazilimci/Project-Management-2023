
menu_answers = ['1', '2', '3', '4', '5']  # accepted inputs for main menu
speed = 0
angle = 0
height = 0


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


def start_new_simulation():
    """
    Starts a new simulation by gathering parameter values:
        - Launch speed
        - Launch angle
        - Launch height
    """

    print("\n")
    print("–" * 36)
    print("  🚀 Starting a New Simulation 🚀")
    print("–" * 36)

    # Obtains the value of launch speed
    while True:
        try:
            speed = float(input("Enter launch speed (in meters per second): "))
            # if input is negative, prints invalid message and asks again
            if speed <= 0:
                print("    ⚠️ Invalid input. Speed must be a positive number\n")
                speed = float(input("Enter launch speed (in meters per second): "))
            break
        # if input is invalid, prints a message
        except ValueError:
            print("    ⚠️ Invalid input. Enter a valid positive number for speed\n")

    # Obtains the value of launch angle
    while True:
        try:
            angle = float(input("Enter launch angle (in degrees): "))
            # if input is zero or less, and/or is greater than or equal to 90,
            # prints invalid message and asks again
            if angle <= 0 or angle >= 90:
                print("    ⚠️ Invalid input. Angle must be a positive number less than 90 degrees\n")
                angle = float(input("Enter launch angle (in degrees): "))
            break
        # if input is invalid, prints a message
        except ValueError:
            print("    ⚠️ Invalid input. Enter a valid positive number for angle\n")

    # Obtains the value of launch height
    while True:
        try:
            height = float(input("Enter launch height (in meters): "))
            # if input is negative, prints invalid message and asks again
            if height < 0:
                print("    ⚠️ Invalid input. Height cannot hold a negative value\n")
                height = float(input("Enter launch height (in meters): "))
            break
        # if input is invalid, prints a message
        except ValueError:
            print("    ⚠️ Invalid input. Enter a valid positive number for height\n")

    # Prints the gathered parameter values
    print("\nParameter Values for Simulation:")
    print("Launch Speed:", speed, "m/s")
    print("Launch Angle:", angle, "degrees")
    print("Launch Height:", height, "m")

    return speed, angle, height


def help():
    """
    Displays the help menu, explaining the program
    and the physics behind the simulation
    https://blog.finxter.com/how-to-print-the-content-of-a-txt-file-in-python/
    """

    # opening the help file and displaying the content
    help_file = open("help.txt")
    help_content = help_file.read()
    print(help_content)


run_code = True

# running code as long as run_code = True
while run_code:

    main_menu()  # displaying the menu
    menu_input = input("➡️ Enter a choice: ").strip()

    # if input is 1, calls function to start new simulation
    if menu_input == "1":
        speed, angle, height = start_new_simulation()

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

    # if input is invalid, prints an appropriate message
    else:
        print("    ⚠️ Sorry that is not a valid choice!")
