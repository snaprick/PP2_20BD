n = int(input())
s = list()
d = dict()
for i in range(n):
    s = input().split()
    #print(s,*s[1])
    for i in range(2,2+int(s[1])):
        d[s[i]]=s[0]
m = int(input())
for i in range(m):
    s1 = str(input())
    if s1 not in d:
        print("Unknown")
    else:
        print(d[s1])