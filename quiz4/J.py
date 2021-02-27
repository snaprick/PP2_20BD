import json
s = input()
x = json.loads(s)
Name = str()
Price = int()
Discount = int()
ans = int()
anss = ""
mn = 111111111
for i in x["Subscriptions"]:
    Price = int(i["price"])
    Name = str(i["name"])
    Discount = int(i["discount"])
    ans = int(Price*(100-Discount)/100)
    #print(Price,(100-Discount)/100,Price*(100-Discount)/100)
    if ans < mn:
        mn=ans
        anss=Name
print("Name:",anss,"\nPrice:",int(mn))