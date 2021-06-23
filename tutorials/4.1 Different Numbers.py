x = 1

# Part 1
while x <= 10:
    cube = x * x * x
    print(f"{x}^3 = {cube}")
    x += 1

x = 1
# Part 2
while x * x < 500:
    if x % 2 == 1:
        square = x * x
        print(f"{x}^2 = {square}")
    x += 1

x = 1
# Part 3
while x ** 2 < 10000:
    print(f"{x}^2 = {x ** 2}")
    x += 1