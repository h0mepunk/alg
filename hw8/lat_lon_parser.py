
str_ = []
while True:
    try:
        line = input().replace('\t', '').replace('[', '').replace(']', '').replace(' ', '')
    except EOFError:
        break
    str_.append(line)


lat = []
lon = []
i = 0
j = 0
k = 0

for i in range(0, len(str_)):
    coords = str_[i].split(",")
    lat.append(coords[0])
    lon.append(coords[1])
    i += 1

for j in range(0, len(lat)):
    print(lat[j], ",")
    j += 1

for k in range(0, len(lon)):
    print(lon[k], ",")
    k += 1

