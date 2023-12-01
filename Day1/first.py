numbers = []
res = 0

with open('input1.txt') as file:
    for line in file:
        aux = []
        for letter in line:
            if letter.isdigit():
                aux.append(int(letter))
        numbers.append(str(aux[0]) + str(aux[len(aux)-1]))

for num in numbers:
    res += int(num)

print(f"The sum of all values is: {res}")