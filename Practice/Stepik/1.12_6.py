a=int(input())
if a == 0:
    print(a,"программистов")
elif a%100 >=11 and a%100 <=14:
    print(a,"программистов")
elif a%10 ==1:
    print(a,"программист")
elif a%10>1 and a%10<5:
    print(a,"программиста")
else:
    print(a,"программистов")