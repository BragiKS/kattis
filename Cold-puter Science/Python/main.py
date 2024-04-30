n = int(input())
T = map(int, input().split())
c = 0
for t in T:
    if t < 0:
        c += 1
print(c)