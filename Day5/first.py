loc = []

with open('example1.txt') as file:
    seeds = file.readline()
    seeds = seeds.split()
    seeds.pop(0)
    for value in seeds:
        aux = []
        for line in file:
            if line == "\n":
                aux = []
            else:
                if not ":" in line:
                    values = line.split()
                    aux.append(values)