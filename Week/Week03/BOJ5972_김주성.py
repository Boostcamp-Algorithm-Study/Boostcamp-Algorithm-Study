import heapq

INF = int(1e9)

n, m = map(int, input().split())  # 노드 수, 간선 수

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)  # 각 노드까지 가는데 필요한 비용 저장

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

start = 1

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))  # (비용, 출발노드)
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    for adj_node in graph[now]:
      cost = dist + adj_node[1]
      if cost < distance[adj_node[0]]:
        distance[adj_node[0]] = cost
        heapq.heappush(q, (cost, adj_node[0]))


dijkstra(start)

print(distance[n])
