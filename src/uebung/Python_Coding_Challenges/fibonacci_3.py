n = 10
for n in range(0, 11):
    if n == 0:
        print("Fibonacci sequence up to", n, ":")
        print(0)
    elif n == 1:
        print(1)
    else:
        list = [0,1]
        i=0
        for i in range(2, n + 1): #
            fibo =list[-1] +list[-2] #explain: sum of last two elements in list
            list.append(fibo)
print(list)