red_cubes = 12
green_cubes = 13
blue_cubes = 14
games = []
res = 0

with open('input1.txt') as file:
    for line in file:
        game = line.split(":")
        num = game[0][5:]
        showed = game[1].split(";")
        var = True
        for cubes in showed:
            cube = cubes.split(",")
            for aux in cube:
                text = aux.split()
                if text[1] == "red" or text[1] == "red\n":
                    if int(text[0]) > red_cubes:
                        var = False
                        break
                if text[1] == "green" or text[1] == "green\n":
                    if int(text[0]) > green_cubes:
                        var = False
                        break
                if text[1] == "blue" or text[1] == "blue\n":
                    if int(text[0]) > blue_cubes:
                        var = False
                        break
        if var:
            games.append(num)

for num in games:
    res += int(num)

print(f"The sum of all values is: {res}")