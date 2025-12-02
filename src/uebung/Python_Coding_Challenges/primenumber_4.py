range_1 = input("Please enter a number1: ")
range_2 = input("Please enter a number2: ")
number_1 = int(range_1)
number_2 = int(range_2)
def isPrime(self):
    if self <= 1:
        return False
    for i in range(2, int(self ** 0.5) + 1): #check divisibility from 2 to square root of self
        if self % i == 0:
            return False
    return True

print("Prime numbers between", range_1, "and", range_2, "are:")
for number in range(int(range_1), int(range_2) + 1):
    if isPrime(number) is True:
        print(number)
    else:
        continue    

