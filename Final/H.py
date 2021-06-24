import sys
a = (str(sys.stdin.read()).split("\n"))
d = dict()
for i in a:
    try:
        x,y = i.split()
        try:
            if int(y) > d[x]:
                d[x] = int(y)
        except:
            d[x] = int(y)
    except:
        continue
for i in sorted(d.keys()):
    print(i,d[i])