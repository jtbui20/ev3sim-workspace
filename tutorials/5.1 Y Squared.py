x = 1
my_squares = []
# Print the square numbers <= 100.
while x * x <= 100:
    # Add to the list.
    my_squares.append(x * x)
    x = x + 1

y = int(input("What square do you want (1-10)? "))

# TODO: print y*y using my_squares
print(my_squares[y - 1])