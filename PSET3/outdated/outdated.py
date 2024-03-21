
month =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]









while True:
    x = input("Date: ")
    y = x.strip().split("/")
    if len(y) == 3:
        if y[0].isalpha():
            pass
        elif int(y[0]) > 12:
            pass
        elif int(y[1]) > 31:
            pass
        else:
            if len(y[0]) <2:
                y[0] = "0" + y[0]
            if len(y[1]) < 2:
                y[1] = "0" + y[1]
            print("%s-%s-%s"%(y[2],y[0],y[1]), end="")
            break
    else:
        y = x.split(" ")
        if " " in y:
            y.remove(" ")
        if "," not in y[1]:
            pass
        else:
            y[1] = y[1].replace(",","")
            if int(y[1]) > 31:
                pass
            else:
                m = month.index(y[0]) + 1
                if m <10:
                    m = "0" + str(m)
                if len(y[1]) < 2:
                    y[1] = "0" + y[1]
                print("%s-%s-%s"%(y[2],m,y[1]), end="")
                break


