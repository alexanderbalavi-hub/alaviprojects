def calculator(delay):
    distance = 10  # distance in kilometers
    travel_time = 7 # travel time in minutes
    delay_min = delay / 60  # convert delay from seconds to minutes
    travel_speed = (distance / (travel_time-delay_min))* 60  # speed in km/h
    print(travel_speed)
    total_time = travel_time + delay_min
    hours = int(total_time // 60)
    minutes = int(total_time % 60)
    return f"The travel_speed is. {travel_speed:.2f} km/h and the total travel time is {hours} hours and {minutes} minutes." 

print("Travel Time Calculator")
while True:
    delay = int(input("Enter delay in seconds: "))
    if delay < 120:
        result = calculator(delay)
        print("", result)
    if delay == 120:
        result = calculator(delay)
        print("Train will be just in Time", result)
    if delay >= 121:
        print("Delay is too high, train will be late.")
        break    