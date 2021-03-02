def f(n):  
    for i in range(1,n+1):  
        a=1
        for j in range(1,i+1):  
            print(a,end=" ")  
            a = int(a*(i-j)/j)
        print("")
n = int(input())
f(n)