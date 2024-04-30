N, M = map(int, input().split())
G = []
c = 0
for i in range(N+M):
    x = int(input())
    if i < N:
        G.append(x)
    else:
        c += 1 if x in G else 0

_ = map(int, input().split())
print(c)