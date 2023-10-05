while True:
    a= input("filename")
    b = ".mp3"
    filename = a+b
    f = open(filename,"w")
    content = input("enter the content you want to enter into file")
    f.write(content)
    f.close()
    f =open(filename,"r")
    print(f.read())
    f.close()
    ex = input("do you want to continue y/n")
    if ex =="y":
        continue
    else :
        exit()