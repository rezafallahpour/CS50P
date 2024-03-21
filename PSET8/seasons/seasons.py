from datetime import date
import inflect
import sys
import re


p = inflect.engine()
def main():
    birthday_str = input("Date of Birth: ")
    try:
        year, month, day = chek(birthday_str)
    except:
        sys.exit("Invalid date")
    birthday = date(int(year),int(month),int(day))
    current_time = date.today()
    time_difference = current_time - birthday
    minutes_passed = time_difference.days*24*60

    minutes_in_words = p.number_to_words(minutes_passed, andword="")

    print(minutes_in_words.capitalize()+" minutes")

def chek(birth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",birth):
        year, month, day = birth.split("-")
        return year, month, day

if __name__ == "__main__":
    main()