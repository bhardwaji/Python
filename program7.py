f= open("hello.txt" ,"r")
print(f.read())  #size as a argument
f.close()


f= open("hello.txt" ,"r")
print(f.read(10))
print(f.read())
print(f.read()) # 2 bar read nahi krega
f.close()


f= open("hello.txt" ,"r")
print(f.readline(10))
print(f.readline(15)) # if data is not present in that line it will get nothing
#another line data will not b readable
print(f.readline())
print(f.readline())

#these functions will not be exicuted because already data is read
print(f.readline())
print(f.readline())




f= open("hello.txt" ,"r")
data =f.readline()
data1 = f.readline()
data2 = f.readline()
print(data,end="")
print(data1,end="")
print(data2,end="")



f= open("hello.txt" ,"r")
data = f.readlines()
print(data)
for i in data :
    print(i,end="")

print(data[0],end="")
print(data[1])
print(data[2])
