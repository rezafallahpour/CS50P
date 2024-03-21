x = input("Greeting: ").lower()
if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
elif x.startswith("w"):
    print("$100")
else:
    print("$0")