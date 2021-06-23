password = "open sesame"

treasure = "Here is your treasure!"

attempt = input("What's the password? ")
count = 1

while (count < 3) and (attempt != password):
    print("Try again!")
    attempt = input("What's the password? ")
    count += 1

if attempt == password:
    print(treasure)
else:
    print("You fail! This program will self destruct in 5, 4, 3 ...")