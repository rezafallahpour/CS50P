import random

while True:
    try:
        number = int(input("Level: "))
        break
    except:
        continue

x = random.randint(1,number)
def inp():
    while True:
        try:
            Guess = int(input("Guess: "))
            return Guess
        except:
            continue
Guess = inp()
while True:
    if Guess > number:
        Guess = inp()
        continue
    if Guess < 0:
        Guess = inp()
        continue
    if Guess > x:
        print("Too large!")
        Guess = inp()
    elif Guess < x:
        print("Too small!")
        Guess = inp()
    else:
        print("Just right!")
        break