res = 1

with open("input1.txt") as file:
    time = file.readline()
    dist = file.readline()

time = time.split()
time.pop(0)

dist = dist.split()
dist.pop(0)

for i in range(len(time)):
    v_ini = 0
    n = 0
    for aux in range (int(time[i])+1):
        t_rema = int(time[i]) - v_ini
        distance = int(dist[i])

        if v_ini * t_rema > distance:
            n += 1

        v_ini += 1
    res *= n

print(f"The mul of all values is: {res}")


#por cada msec, aumenta la velocidad 1msec/mm
#solo se mueve cuando dejas de pulsar el botón