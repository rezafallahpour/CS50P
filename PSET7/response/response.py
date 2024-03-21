from validator_collection import validators, checkers, errors

def main():
    print(is_valid(input("What's your email address? ")))




def is_valid(s):
    try:
        email_address = validators.email(s)
        return "Valid"
    except:
        return "Invalid"





if __name__ == "__main__":
    main()
