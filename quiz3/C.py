n = int(input())
a = list(map(int,input().split()))
s = set()
j = 1
for i in a:
    s.add(i)
s= sorted(s,key=int)
for i in s:
    print(j,i)
    j+=1