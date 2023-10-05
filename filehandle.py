
try :
    f =open("hello.txt","r")
    # f.write("hello")
    print(f.read())
except Exception as e:
    print(e)

