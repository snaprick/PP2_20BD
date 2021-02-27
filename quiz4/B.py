import re
s = input()
s1 = input()
s2= re.compile(s1)
ans = s2.search(s)
try:
    print("First time {} occured in position: {}".format(s1,ans.start()))
except:
    print("Not found")