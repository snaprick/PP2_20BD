def make_bold(n):
    return "<b>{}</b>".format(n)

def make_italic(n):
    return "<i>{}</i>".format(n)

def make_underline(n):
    return "<u>{}</u>".format(n)
print("1:Bold")
print("2:Italic")
print("3:Underline")
i = int(input("Input :"))
print("Write your string")
s = input("Input :")
if i == 1:
    print(make_bold(s))
if i == 2:
    print(make_italic(s))
if i == 3:
    print(make_underline(s))