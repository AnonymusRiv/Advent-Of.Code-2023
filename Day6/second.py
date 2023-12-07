res = 1
time_value = ""
dist_value = ""

with open("input2.txt") as file:
    time = file.readline()
    dist = file.readline()

time = time.split()
time.pop(0)
dist = dist.split()
dist.pop(0)

for item in time:
    time_value += item

for item in dist:
    dist_value += item

v_ini = 0
n = 0

for aux in range (int(time_value) + 1):
    t_rema = int(time_value) - v_ini
    distance = int(dist_value)

    if v_ini * t_rema > distance:
        n += 1

    v_ini += 1
res *= n

print(f"The mul of all values is: {res}")


#por cada msec, aumenta la velocidad 1msec/mm
#solo se mueve cuando dejas de pulsar el botón