import inflect

p = inflect.engine()
mylist = ["Adieu, adieu, to Liesl"]
while True:
    try:
        x = input("Name: ")
        if x.lower() != "liesl":
            mylist.append(x)
    except:
        print()
        break
mylist = tuple(mylist)
print(p.join((mylist)).replace(";",","))

