x = input("File name: ").lower()
x = x.split(".")
if len(x) == 1:
    print("application/octet-stream")
elif x[-1] == "gif":
    print("image/gif")
elif x[-1] == "jpg" or x[-1] == "jpeg":
    print("image/jpeg")
elif "pdf" in x[-1]:
    print("application/pdf")
elif x[-1] == "png":
    print("image/png")
elif x[-1] == "txt":
    print("text/plain")
elif x[-1] == "zip":
    print("application/zip")
elif x[-1] == "bin":
    print("application/octet-stream")







