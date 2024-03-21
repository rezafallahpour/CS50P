print("Amount Due: 50")

x = 50
while x > 0:
    y = int(input("Insert Coin: "))
    if y == 25 and x-y > 0:
        x = x-y
        print("Amount Due: %i"%x)
    elif y == 25 and x-y == 0:
        x = x-y
        print("Change Owed: 0")
    elif y == 10 and x-y > 0:
        x = x-y
        print("Amount Due: %i"%x)
    elif y == 10 and x-y == 0:
        x = x-y
        print("Change Owed: 0")
    elif y == 5 and x-y > 0:
        x = x-y
        print("Amount Due: %i"%x)
    elif y == 5 and x-y == 0:
        x = x-y
        print("Change Owed: 0")
    else:
        print("Amount Due: %i"%x)