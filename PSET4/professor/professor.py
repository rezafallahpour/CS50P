import random


def main():
    level = get_level()
    score = ssim(level)
    print("Score: ",score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level ==1:
        x  = random.randint(0,9)
        y  = random.randint(0,9)
    elif level == 2:
        x  = random.randint(10,99)
        y  = random.randint(10,99)
    else:
        x  = random.randint(100,999)
        y  = random.randint(100,999)
    return x,y

def simround(x , y):
    count = 1
    while count <= 3:
        try:
            ans = int(input("%i + %i = "%(x,y)))
            if ans == (x+y):
                return True
            else:
                count +=1
                print("EEE")
        except:
            count +=1
            print("EEE")
    print("%i + %i = %i"%(x,y,x+y))
    return False

def ssim(level):
    score = 0
    for i in range(10):
        x , y = generate_integer(level)
        res = simround(x , y)
        if res == True:
            score +=1
    return score



if __name__ == "__main__":
    main()