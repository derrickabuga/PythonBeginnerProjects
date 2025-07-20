# Formula for finding the nth term in AP:
    # n = a + (n - 1)d
n = int(input("How many terms do you want? "))
a = int(input("Where would you like to start? "))
d = int(input("What is the common difference? "))

arithmetic_progression = []

if n > 100:
    print("ERROR: OUT OF ACCEPTABLE RANGE")
else:
    for x in range(a, n+1):
        if x == a:
            arithmetic_progression += str(x)
        else:
            x += d
            arithmetic_progression += str(x)
    print(arithmetic_progression)
        