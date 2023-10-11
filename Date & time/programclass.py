import string

while True:
    name = input("Enter the name").upper()
    for i in name:
     print(i)
    if not(i in string.ascii_letters):
        print("you cant enter digit or puntuations in name")

    else:
        break

    if i in string.ascii_letters:
        if len(name)>10:
          print("name is greater then 10 please enter again")

    else:
        print(name)
        break

