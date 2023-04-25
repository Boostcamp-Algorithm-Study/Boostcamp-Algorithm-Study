import sys
N = int(input())
M = int(input())
INF = sys.maxsize

cost = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1],c)
    
for i in range(N):
    for j in range(N):
        for k in range(N):
            cost[j-1][k-1] = min(cost[j-1][k-1], cost[j-1][i-1]+cost[i-1][k-1])
      
for i in range(N):
    for j in range(N):
        if i == j or cost[i-1][j-1] == INF:
            cost[i-1][j-1] = 0
    
for arr in cost:
    print(*arr)