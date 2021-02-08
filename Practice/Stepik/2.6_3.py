a = list(map(int,input().strip().split()))
n = int(input())
cnt=0
m=[]
for i in a:
    if i == n:
        m.append(cnt)
    cnt+=1
if len(m)==0:
    print("Отсутствует")
    exit
for i in m:
    print(i,end=' ')