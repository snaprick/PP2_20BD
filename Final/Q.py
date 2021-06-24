n, m = map(int,input().split())
for i in range(n):
    for j in range(m):
        if i < n//2 and j <m//2:
            print(1,end=" ")
        elif i>=n//2 and j < m//2:
            print(2,end=" ")
        elif i>=n//2 and j >= m//2:
            print(3,end=" ")
        else:
            print(0,end=" ")
    print()