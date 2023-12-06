res = 0
copy = [1] * 11

with open('input2.txt') as file:
    for line in file:
        info = line.split(":")
        numbers = info[1].split("|")
        winn = numbers[0].split()
        mynum = numbers[1].split()
        i = 0
        for t in range(copy[0]):
            for num in winn:
                for aux in mynum:
                    if int(num) == int(aux):
                        i+= 1

        res += copy[0]
        
        for j in range(1, (i//copy[0]+1), 1):
            copy[j] += copy[0]

        copy.pop(0)
        copy.append(1)

print(f"The sum of all values is: {res}")