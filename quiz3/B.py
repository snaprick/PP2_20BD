import re
txt = input()
x = re.search(r"[A-Z]", txt)
y = re.search(r"[a-z]",txt)
z = re.search(r"\d",txt)
f = re.search(r"_",txt)
if x and y and z and f:
  print("Found a match!")
else:
  print("Not matched!")
