x = input("camelCase: ")
print("snake_case: ", end = "")
for i in range(len(x)):
    if x[i].isupper() and i>0:
        print("_", end = "")
    print(x[i].lower(), end = "")
print()




