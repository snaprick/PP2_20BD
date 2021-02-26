import sys
d = dict()
s = set()
a = (str(sys.stdin.read()).split())
for i in a:
    d[i] = d.get(i, 1) + 1
for i in d:
    if(d[i]%2==1):
        s.add(i)
s = sorted(s,key=str)
for i in s:
    print(i)