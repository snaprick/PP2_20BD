import math
s=str(input())
if s == "треугольник":
    a=int(input())
    b=int(input())
    c=int(input())
    p=(a+b+c)/2
    print(math.sqrt(p*(p-a)*(p-b)*(p-c)))
elif s == "прямоугольник":
    a=int(input())
    b=int(input())
    print(a*b)
else:
    r=int(input())
    print(3.14*r*r)