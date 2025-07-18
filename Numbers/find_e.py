import math

e = math.e
num = int(input("Enter a number: "))
if num > 100:
    print("Out of acceptable range")
else:
    print(round(e, num))