
# text mode pe encoding hoti hai
f = open("./hello.txt", "r")
print(f.read())
f.close()

# encoding nahi hoti in binary mode
f = open("./hello.txt","rb")
print(f.read())
f.close()

#rb ,wb ,ab ,xb ,rb+ ,wb++, ab+  = modes in binary