

def main():
    while True:
        print("choose your operation:")
        print("1. add")
        print("2. subtract")
        print("3. multipy")
        print("4. divided")
        print("5. exit")

        choice = input("type your action: ")

        if choice == '5':
            print("Good bye")
            break

        num1 = float(input("input yourr first number: "))
        num2 = float(input("input yourr second number: "))

        if choice == '1':
            print("result of add: ", str(add(num1, num2)))
        elif choice == '2':
            print("result of subtract: ", str(subtract(num1, num2)))
        elif choice == '3':
            print("result of multiply: ", str(multiply(num1, num2)))
        elif choice == '4':
            print("result of divided: ", str(divide(num1, num2)))
        else:
            print("error you enter a wrong number please try again")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "error: The denominator of the fraction is zero "
    else:
        return x / y
if __name__ == "__main__":
    main()
