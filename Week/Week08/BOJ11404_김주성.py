import math 

INF = math.inf   

n = int(input()) 
m = int(input()) 

graph = [[INF] * (n+1) for _ in range(n+1)] 

for a in range(1, n+1): 
    for b in range(1, n+1): 
        if a == b: 
            graph[a][b] = 0  

for _ in range(m): 
    a, b, cost = map(int, input().split()) 
    if cost < graph[a][b]: 
        graph[a][b] = cost  

# 플로이드 워셜 알고리즘 
for k in range(1, n+1): 
    for a in range(1, n+1): 
        for b in range(1, n+1): 
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])  # 다이나믹 프로그래밍 점화식 

for a in range(1, n+1): 
    for b in range(1, n+1): 
        if graph[a][b] == INF: 
            print(0, end=' ') 
        else: 
            print(graph[a][b], end=' ') 
    print()
