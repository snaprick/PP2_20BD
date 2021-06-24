def convert(n):
    ans = list()
    if n == 0:
        print(0)
    while n>0:
        ans.append(n%7)
        n //= 7 
    print(*ans[::-1],sep="")
n = int(input())
convert(n)