import sys
a = (str(sys.stdin.read()).split())
d = dict()
for i in a:
    d[i] = d.get(i,0)+1
for i in sorted(d.keys()):
    print(i,d[i])