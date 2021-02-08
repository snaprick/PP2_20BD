a=int(input())
sum=a//100000+a//10000%10+a//1000%10
sum1=a//100%10+a//10%10+a%10
if sum==sum1:
    print("Счастливый")
    #print(sum,"\n",sum1)
else:
    print("Обычный")
    #print(sum,"\n",sum1)