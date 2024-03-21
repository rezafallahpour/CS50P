import requests
import sys
import json


def main():
    parameter = argu()
    rat = data()
    z = rat * parameter
    print(f"${z:,.4f}")


def data():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    x = response.json()
    z = float(x["bpi"]["USD"]["rate_float"])
    return z


def argu():
    if len(sys.argv) !=2:
        sys.exit("Missing command-line argument")
    try:
        x = float(sys.argv[1])
        return x
    except:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()
