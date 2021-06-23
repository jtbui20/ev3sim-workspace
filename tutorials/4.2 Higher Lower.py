p1 = int(input("Player 1 please enter a number: "))

while True:
    p2 = int(input("Player 2 please enter a number: "))
    if p2 == p1:
        print("Success")
        break
    elif p2 > p1:
        print("Lower")
    elif p2 < p1:
        print("Higher")
    else:
        print("????")