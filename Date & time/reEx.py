import re
txt = "hello my name is shubham"
x = re.search("name is",txt)
if x:
    print("true")
else:
    print("false")
