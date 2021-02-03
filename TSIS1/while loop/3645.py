a = int(input())
while a!=0:
    if a%2==0 or a==1:
        a=a//2
    else:
        print("NO")
        exit()
print("YES")