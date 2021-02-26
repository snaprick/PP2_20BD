import re
txt = input()
x = re.search(r"[A-Z][a-z]+", txt)

if x:
  print("Found a match!")
else:
  print("Not matched!")
