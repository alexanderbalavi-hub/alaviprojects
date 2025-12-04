#create list with value 1 to 49
lotto_numbers = list(range(1, 50))
winning_numbers = list()
import random
#shuffle the list
for i in range(7):
    #select first number of the list
    random.shuffle(lotto_numbers)
    number = lotto_numbers[0]
    #add number to winning numbers
    winning_numbers.append(number)
    #pop the first number from the list
    lotto_numbers.pop(0)
    #select next number by increasing i
    i += 1
print(lotto_numbers)
print("The winning lotto numbers are: ", winning_numbers)

