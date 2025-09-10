colors = []
while True:
    color = input("Enter a color: ")
    if color in colors:
        colors.append(color)
        print(colors)
    else:
        break