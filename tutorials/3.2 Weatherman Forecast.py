celsius = int(input("What is the celsius reading today: "))

if celsius < 23:
    if celsius > 7:
        if celsius >= 18:
            print("Have a great day!")
        else:
            print("Chances of rain, take an umbrella")
    else:
        print("Stay inside and rug up!")
else:
    if celsius < 32:
        print("Remember to wear sunscreen when leaving!")
    else:
        print("Stay cool and hydrated. Extreme fire danger.")