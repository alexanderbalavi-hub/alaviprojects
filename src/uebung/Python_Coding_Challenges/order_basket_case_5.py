basket = {}

while True:
    product = input("Enter product name: ")
    amount = int(input("Enter amount: "))
    basket[product] = amount
    exitorout = input("Do you want to add more products? (o/e): ").lower()
    if exitorout== "o":
        print(basket)
    elif exitorout == "e":
        print("Your order has been placed.")
        break

    else:
        print("Thank you for visiting the shop.")



