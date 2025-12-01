#First Challenge
#read in a number from the user
user_input = input("Please enter a number: ")
#check if the input is a number
#only read out the number out of strings less than or equal to 10
try:
    number = float(user_input)
    if number <= 10:
        print(f"You entered the number: {number}")
    else:
        print("The number is greater than 10.")
except ValueError:
    print("That's not a valid number.")



