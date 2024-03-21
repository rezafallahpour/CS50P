



def main():
    word = input("Input: ")
    s = shorten(word)
    print(s)



def shorten(word):
    w = []
    for i in word:
        if i in ["A","a","E","e","I","i","O","o","U","u"]:
            continue
        w.append(i)
    my_string = "".join(w)
    return my_string


if __name__ == "__main__":
    main()