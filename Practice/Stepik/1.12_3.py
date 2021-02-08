a=float(input())
b=float(input())
c=str(input())
if c == "mod" and b!=0.0:
    print(a%b)
elif c=="mod":
    print("Деление на 0!")
if c == "div" and b!= 0.0:
    print(a//b)
elif c=="div":
    print("Деление на 0!")
if c == "pow":
    print(pow(a,b))
if c == "+":
    print(a+b)
if c == "-":
    print(a-b)
if c == "*":
    print(a*b)
if c == "/" and b != 0.0:
    print(a/b)
elif c=="/":
    print("Деление на 0!")