import sys
a = (str(sys.stdin.read()).split())
d = dict()
for i in a:
    d[(i.lower()[0])] = d.get(i.lower()[0],0)+1
for i in range(97,123):
    try:
        print(d[chr(i)])
    except:
        print(0)