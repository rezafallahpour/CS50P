
def main():
    x = divided()
    

def divided():
    while True:
            try:
                x = input("Fraction: ").split("/")
                z = (int(x[0])/int(x[1]))*100
                if z <= 100:
                    return z
                else:
                    pass
            except (ValueError, ZeroDivisionError):
                pass

main()