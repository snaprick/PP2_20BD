s = input()
cntu=0
cntl=0
for i in s:
    if i.isupper():
        cntu+=1
    if i.islower():
        cntl+=1
print("No. of Upper case characters :",cntu)
print("No. of Lower case Characters :",cntl)