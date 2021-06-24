n = int(input())
data = {}
for i in range(n):
    name, value = input().split()
    value = int(value)
    try: 
        data[name] += value
    except KeyError:
        data[name] = value

total = sum(data.values())
data = {
    name: value / total * 100.0
    for name, value in data.items()
}

data_l = list(data.items())

for i in range(len(data_l)):
    for j in range(i + 1, len(data_l)):
        if data_l[i][1] < data_l[j][1]:
            tmp = [*data_l[i]]
            data_l[i] = data_l[j]
            data_l[j] = tmp
        elif data_l[i][1] == data_l[j][1]:
            if data_l[i][0] < data_l[j][0]:
                tmp = [*data_l[i]]
                data_l[i] = data_l[j]
                data_l[j] = tmp

data = dict(data_l)

for name, value in data.items():
    print(name, "%g" % (value) + "%")