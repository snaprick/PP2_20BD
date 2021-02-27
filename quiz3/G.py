n = int(input())
s = set()   
s1 = set()
s2 = set()
for i in range(n):
    a = input()
    if i == 0:
        for j in a:
            s.add(j)
    for j in a:
        s1.add(j)
    s=s.intersection(s1)
    s1.clear()
s=sorted(s,key=str)
if s:
    for i in s:
        print(i,end = " ")
else:
    print("NO COMMON CHARACTERS")
