import math
import matplotlib.pyplot as plt

menu_answers = ['1', '2', '3', '4', '5']  # accepted inputs for main menu

G = 9.81  # m/s^2


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
    print("–" * 32)
    print("Launch Speed:", speed, "m/s")
    print("Launch Angle:", angle, "degrees")
    print("Launch Height:", height, "m")

    return speed, angle, height


def calculate_projectile_motion(speed, angle, height):
    """
    Calculates projectile motion using physics equations.
    Returns motion data for plotting the motion graph.
    Also calculates and returns total flight duration, maximum height, and horizontal range.
    """

    # Converts angle from degrees to radians
    angle_rad = math.radians(angle)

    # calculates initial x and y velocity components
    initial_velocity_x_component = speed * math.cos(angle_rad)
    initial_velocity_y_component = speed * math.sin(angle_rad)

    # calculates total time of flight of projectile
    flight_duration = 2 * initial_velocity_y_component / G

    # calculates maximum height reached by projectile
    max_height = height + (initial_velocity_y_component ** 2 / (2 * G))

    # calculates horizontal range of projectile
    horizontal_range = speed ** 2 * math.sin(2 * angle_rad) / G

    # dictionary for storing motion data x and y (displacement) values at time increments
    motion_data = {}

    # Loop calculates motion at each time increment
    time_increments = flight_duration / 100  # 100 time points for smoother graph
    for time in range(101):
        time = time * time_increments

        distance_t = initial_velocity_x_component * time
        height_t = height + (initial_velocity_y_component * time) - (0.5 * G * time ** 2)

        # motion data is added to dictionary until projectile hits the ground
        if height_t >= 0:
            motion_data[distance_t] = height_t

    return motion_data, flight_duration, max_height, horizontal_range


def display_motion_data():
    """
    function displays the motion data, including:
        - total flight time
        - maximum height
        - horizontal range
    """

    print("\nMotion Data:")
    print("–" * 12)
    print("Total Flight Time:", f'{flight_duration:.2f}', "s")
    print("Maximum Height:", f'{max_height:.2f}', "m")
    print("Horizontal Range:", f'{horizontal_range:.2f}', "m")


def graph_projectile_motion():
    """
    Plots the projectile motion graph using matplotlib.
    """

    # creating a list of the x and y values using motion_data dictionary
    x_values = list(motion_data.keys())
    y_values = list(motion_data.values())

    # plotting graph
    plt.plot(x_values, y_values, marker=".", linestyle=" ")

    # labeling the graph axis and title
    plt.title("Projectile Motion Displacement Graph")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)

    plt.show()


def export_data():
    """
    Exports motion data, flight duration, max height, and horizontal range to a text file.
    """

    # creating a file and adding motion data
    with open("motion_data_export", 'w') as file:
        file.write("Motion Data:\n")
        file.write("Distance (m), Height (m)\n")
        # loop iterates through motion_data dictionary,
        # adding the displacement (x and y) values to the text file
        for distance, height in motion_data.items():
            file.write(f"{distance}, {height}\n")
        file.write("\n")

        # adding flight statistics to motion_data text file
        file.write("Flight Information:\n")
        file.write(f"Total Flight Time: {flight_duration} seconds\n")
        file.write(f"Maximum Height: {max_height} meters\n")
        file.write(f"Horizontal Range: {horizontal_range} meters\n")

    print("      ✅ File Exported.\n")


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
parameter_set = False

# running code as long as run_code = True
while run_code:

    main_menu()  # displaying the menu
    menu_input = input("➡️ Enter a choice: ").strip()

    # if input is 1, calls function to start new simulation
    if menu_input == "1":
        speed, angle, height = start_new_simulation()
        motion_data, flight_duration, max_height, horizontal_range = calculate_projectile_motion(speed, angle, height)
        parameter_set = True

    # if input is 2, calls function to display motion graph and data
    elif menu_input == "2":
        # if parameters have been set, displays projectile motion –
        # else displays an appropriate message
        if not parameter_set:
            print("    ⚠️ Please start a new simulation (option 1) first")
        else:
            display_motion_data()
            graph_projectile_motion()

    # if input is 3, calls function to export motion data as file
    elif menu_input == "3":
        # if parameters have been set, exports motion data –
        # else displays an appropriate message
        if not parameter_set:
            print("    ⚠️ Please start a new simulation (option 1) first")
        else:
            export_data()

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

print("\nThank you for using this Projectile Motion Simulation.")
