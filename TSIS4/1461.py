b = list(map(int, input().split()))
for i in range(len(b) - 2):
    if b[i] == b[i + 1] and b[i] == b[i + 2]:
        b[i:i + 3] = [-1, -1, -1]
print(len([i for i in b if i != -1]))
