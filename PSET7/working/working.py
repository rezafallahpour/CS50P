import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
        try:
            if fa:= re.search(r"^(\d{1,2}) (\w{2}) to (\d{1,2}) (\w{2})",s):
                ga = fa.groups()
                first = int(ga[0])
                second = int(ga[2])
                if ga[1].upper() == "PM":
                    first += 12
                if ga[3].upper() == "PM":
                    second += 12
                return ("{:02d}:00 to {:02d}:00".format(first,second))
            else:
                fb =re.search(r"^(\d{1,2}):(\d{2}) (\w{2}) to (\d{1,2}):(\d{2}) (\w{2})",s)
                gb = fb.groups()
                firsth = int(gb[0])
                ffm = int(gb[1])
                firstm = gb[1]
                secondh = int(gb[3])
                ssm = int(gb[4])
                secondm = gb[4]
                if ffm > 59 or ffm < 0:
                    sys.exit("ValueError")
                if ssm > 59 or ssm < 0:
                    sys.exit("ValueError")
                if gb[2].upper() == "PM":
                    firsth += 12
                if gb[5].upper() == "PM":
                    secondh += 12
                return ("{:02d}:{} to {:02d}:{}".format(firsth,firstm,secondh,secondm))
        except:
            sys.exit("ValueError")




if __name__ == "__main__":
    main()
