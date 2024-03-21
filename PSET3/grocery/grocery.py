def main():
    L = {}
    L = item()
    sorted_dict = dict(sorted(L.items()))
    for i in sorted_dict:
        print("%i %s" % (sorted_dict[i], i))

def item():
    z = {}
    while True:
        try:
            item = input().upper()
            if item in z:
                z[item] += 1
            else:
                z[item] = 1
        except EOFError:
            return z
main()
