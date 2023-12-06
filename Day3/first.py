res = 0
text = []
num = []

with open('example1.txt') as file:
    f = file.read()

f = f.split()
for lines in f:
    line = lines.split()
    text.append(line)

i = 0
for elem in text:
    for aux in elem:
        j = 0
        for car in aux:
            

            if car != "." and not car.isdigit():
                #superior
                if i != 0:
                    #izquierda
                    if j != 0 and f[i-1][j-1].isdigit():
                        k = j - 1
                        num_ant = ""
                        while k >= 0 and f[i-1][k].isdigit():
                            num_ant = f[i-1][k] + num_ant
                            k -= 1
                        num.append(num_ant)

                    #superior
                    elif f[i-1][j].isdigit():
                        k = j
                        num_ant = ""
                        while k < len(f[i-1])-1 and f[i-1][k].isdigit():
                            num_ant = num_ant + f[i-1][k]
                            k += 1
                        num.append(num_ant)
                    
                    #derecha
                    elif f[i-1][j+1].isdigit():
                        k = j + 1
                        num_ant = ""
                        while k < len(f[i-1])-1 and f[i-1][k].isdigit():
                            num_ant = num_ant + f[i-1][k]
                            k += 1
                        num.append(num_ant)

                #derecha
                if aux[j-1].isdigit():
                    k = j - 1
                    num_ant = ""
                    while k >= 0 and aux[k].isdigit():
                        num_ant = aux[k] + num_ant
                        k -= 1
                    num.append(num_ant)
                
                #izquierda
                if aux[j+1].isdigit():
                    k = j + 1
                    num_ant = ""
                    while k < len(aux-1) and aux[k].isdigit():
                        num_ant = aux[k] + num_ant
                        k += 1

                """ #inferior
                if i != 0:
                    #izquierda
                    if j != 0 and f[i+1][j-1].isdigit():
                        k = j - 1
                        num_ant = ""
                        while k >= 0 and f[i-1][k].isdigit():
                            num_ant = f[i-1][k] + num_ant
                            k -= 1
                        num.append(num_ant)

                    #superior
                    elif f[i-1][j].isdigit():
                        k = j
                        num_ant = ""
                        while k < len(f[i-1])-1 and f[i-1][k].isdigit():
                            num_ant = num_ant + f[i-1][k]
                            k += 1
                        num.append(num_ant)
                    
                    #derecha
                    elif f[i-1][j+1].isdigit():
                        k = j + 1
                        num_ant = ""
                        while k < len(f[i-1])-1 and f[i-1][k].isdigit():
                            num_ant = num_ant + f[i-1][k]
                            k += 1
                        num.append(num_ant)"""

            j += 1
        i += 1

for numbers in num:
    res += int(numbers)

print(f"The sum of all values is: {res}")
