from pyfiglet import Figlet
import sys

x = sys.argv[2]
if sys.argv[1].lower() == "-f" or sys.argv[1].lower() == "--font" :
    try:
        f = Figlet(font='%s'%x)
        text = input("Input: ")
        print("Output: ",f.renderText('%s'%text))

    except:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")




