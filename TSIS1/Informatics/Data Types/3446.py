ans=0
cnt=1
for i in range (1,11):
    if i%2==0:
        ans-=4/cnt
    else:
        ans+=4/cnt
    cnt+=2
print(ans)