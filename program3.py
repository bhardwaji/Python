def readable():
    print(f.readable())
def writeable():
    print(f.writable())
def spaces():
    print('''
    
    ''')

f = open("hello.txt" ,"w")
readable()
writeable()
spaces()
f = open("hello.txt" ,"r")
readable()
writeable()
spaces()
f = open("hello.txt" ,"a")
readable()
writeable()
spaces()
f = open("hello.txt" ,"r+")
readable()
writeable()
spaces()
f = open("hello.txt" ,"w+")
readable()
writeable()
spaces()
f = open("hello.txt" ,"a+")
readable()
writeable()
spaces()
f = open("hello.txt" ,"x")
readable()
writeable()
spaces()