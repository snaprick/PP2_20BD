a,b= map(int,input().split())
cnt=0
while(a<=b):
    a*=3
    b*=2
    cnt+=1
print(cnt)