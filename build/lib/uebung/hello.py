import numpy as np
a = int(input("Gebe zahl ein"))
class Dice():
    def rollDice(self, a):
        msg = "Roll a dice!"
        print(msg)
        i = 0
        while i < a:
            print(np.random.randint(1,9))
            i +=1
obj = Dice()
obj.rollDice(a)
