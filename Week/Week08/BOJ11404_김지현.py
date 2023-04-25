# 11404 플로이드
import heapq

n = int(input()) # 도시 수
m = int(input()) # 버스 수

INF = float('inf')

graph = [[] for _ in range(n+1)]
for i in range(m) :
    a,b,c = map(int, input().split()) # 출발, 도착, 비용
    graph[a].append((c,b))
    

# 다익스트라 알고리즘
def cal_cost(start_city):
    queue = []
    costs = [INF] * (n+1)
    heapq.heappush(queue, (0, start_city))
    
    while queue :
        cost, city = heapq.heappop(queue)
        if cost > costs[city] :
            continue
        for next_cost, next_city in graph[city] :
            if next_cost+cost < costs[next_city] :
                costs[next_city] = next_cost + cost
                heapq.heappush(queue, (costs[next_city], next_city))
    
    costs[start_city] = 0
    del costs[0]
    
    for i in range(n) :
        if costs[i] == INF :
            costs[i] = 0 
    
    return costs

# 출력
for i in range(1,n+1) :
    print(*cal_cost(i))
