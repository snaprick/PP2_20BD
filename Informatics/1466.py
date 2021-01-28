a = int(input())
ans=0
if a >= 0:
    print(int(((1+a)*a)//2))
else:
    a=abs(a)
    print(int(-((1+a)*a)//2)+1)
