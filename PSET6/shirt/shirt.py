import sys
import os
from PIL import Image, ImageOps


def main():
    start()
    # Open the shirt image
    shirt = Image.open(sys.argv[1])

    shirt_png = Image.open('shirt.png')

    size = shirt_png.size

    new = ImageOps.fit(shirt, size)

    new.paste(shirt_png, shirt_png)
    # Save the modified image with the provided output filename
    new.save(sys.argv[2])

def start():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[2].endswith("png") or sys.argv[2].endswith("jpg"):
            s , e = os.path.splitext(sys.argv[1])
            s1 , e1 = os.path.splitext(sys.argv[2])
            if e != e1:
                sys.exit("Input and output have different extensions")
            try:
                with open("%s"%sys.argv[1], "r") as file:
                    return True
            except FileNotFoundError:
                sys.exit("Input does not exist")
        if not sys.argv[2].endswith("png") or not sys.argv[2].endswith("jpg"):
            sys.exit("Invalid output")



if __name__ == "__main__":
    main()