password = "open sesame"

treasure = "Here is your treasure!"

attempt1 = input("What's the password? ")
if attempt1 == password:
    print(treasure)
else:
    print("Try again!")
    attempt2 = input("What's the password? ")
    if attempt2 == password:
        print(treasure)
    else:
        attempt2 = input("What's the password? ")
        if attempt2 == password:
            print(treasure)
        else:
            print("You fail! This program will self destruct in 5, 4, 3 ...")