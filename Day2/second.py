res = 0

with open('input2.txt') as file:
    for line in file:
        game = line.split(":")
        num = game[0][5:]
        showed = game[1].split(";")
        red = 0
        green = 0
        blue = 0
        for cubes in showed:
            cube = cubes.split(",")
            for aux in cube:
                text = aux.split()
                if text[1] == "red" or text[1] == "red\n":
                    if int(text[0]):
                        red = max(red, int(text[0]))
                if text[1] == "green" or text[1] == "green\n":
                    if int(text[0]):
                        green = max(green, int(text[0]))
                if text[1] == "blue" or text[1] == "blue\n":
                    if int(text[0]):
                        blue = max(blue, int(text[0]))
        mul = red * green * blue
        res += mul


print(f"The sum of all values is: {res}")