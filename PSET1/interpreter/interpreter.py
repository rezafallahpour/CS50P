x = input("Expression: ").split(" ")
a = float(x[0])
b = x[1]
c = float(x[2])
if b == "/":
    print(a/c)
elif b == "*":
    print(a*c)
elif b == "+":
    print(a+c)
elif b == "-":
    print(a-c)