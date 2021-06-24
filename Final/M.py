s = input()
d = dict()
for i in s:
    d[i] = d.get(i,0)+1
print(len(d))
for i in sorted(d.keys()):
    print(i,d[i])