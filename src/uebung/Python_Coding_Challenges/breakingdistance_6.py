def calculate_breaking_distance(velocity, reaction_time, friction_coefficient):
    # Breaking distance formula
    return (velocity / 10) ** 2 / (2 * friction_coefficient) + (velocity / 3.6) * reaction_time

while True:
    print("Please enter the speed of the vehicle in km/h:")
    initial_speed = float(input())
    print("Please enter the reaction time of the driver in seconds:")
    reaction_time = float(input())
    print("Please enter the ground condition d(ry), w(et), i(ced):")
    ground_condition = input().lower()
    if ground_condition == 'd':
        friction_coefficient = 0.8
    elif ground_condition == 'w':
        friction_coefficient = 0.6
    else:
        friction_coefficient = 0.2

    breaking_distance = calculate_breaking_distance(initial_speed, reaction_time, friction_coefficient)
    print(f"The breaking distance is: {breaking_distance:.2f} meters")
    print("Do you want to calculate again? (y/n):")
    again = input().lower()
    if again != 'y':
        print("Thank you for using the breaking distance calculator.")
        break
