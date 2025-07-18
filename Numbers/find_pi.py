import math

pi = math.pi
num = int(input("Enter a number: "))
if num > 100:
    print("Out of accetable range")
else:
    print(round(pi, num))