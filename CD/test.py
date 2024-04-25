N, M = map(int, input().split())
G = []
c = 0
i = 0
while(1):
    x = map(int, input().split()) if i >= N+M else int(input())
    if i < N:
        G.append(x)
    elif i < N+M:
        c += 1 if x in G else 0
    else:
        A, B = x 
        if A == 0 and B == 0:
            break
    i += 1

print(c)