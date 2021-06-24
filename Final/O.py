import sys
a = (str(sys.stdin.read()).split())
d = dict()
for i in a:
    d[i.upper()] = d.get(i.upper(),0)+1
mx = -1
mi = 0
for i in d.keys():
    if d[i]>mx:
        mx = d[i]
        mi = i
print(mi)