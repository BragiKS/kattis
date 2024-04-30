from sys import stdin

N = int(input())
G = []
for i in range(N):
    G.append(stdin.readline().strip())

lines = stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    a -= 1
    b -= 1
    G[a] = G[a] + G[b]
    G[b] = ""

print(G[a])