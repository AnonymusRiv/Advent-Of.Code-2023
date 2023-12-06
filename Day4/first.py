res = 0

with open('input1.txt') as file:
    for line in file:
        info = line.split(":")
        numbers = info[1].split("|")
        winn = numbers[0].split()
        mynum = numbers[1].split()
        i = 0
        for num in winn:
            for aux in mynum:
                if int(num) == int(aux):
                    i+= 1
        if i != 0:
            res += 2 ** (i -1)

print(f"The sum of all values is: {res}")