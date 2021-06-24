import sys
a = (str(sys.stdin.read()).split())
b = list()
c = list()
s = ''.join(sorted(a[0]))
for i in a[1:]:
    ss = ''.join(sorted(i))
    if not ss == s:
        c.append(i)
print(*sorted(c))