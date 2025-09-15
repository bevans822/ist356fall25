colors = []
while True:
    color = input("Enter a color: ")
    if color == "quit":
        break
    elif color in colors:
        print(colors)
    else:
        colors.append(color)
        print(colors)
    