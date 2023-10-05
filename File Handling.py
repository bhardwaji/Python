f = open("hello.txt", "w",encoding="utf-8")
f.write("Helllo World How are you")
print(f)
f = open("hello.txt")
print(f)
print(f.read())
f.close()

name = "hello"
age = 18
f = open("hello.txt","w")
f.write(f"the name of person is {name} \nand age of person is {age} \nnow we are happy")
f.close()
f= open("hello.txt")
print(f.read(2))

print(f.readline())
print(f.readline())
print(f.readline())


