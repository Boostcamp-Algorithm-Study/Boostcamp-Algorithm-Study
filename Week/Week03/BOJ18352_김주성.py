from collections import deque

# 도시의 개수, 도로의 개수, 거리, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]  

for _ in range(m):  
  a, b = map(int, input().split())  # 단방향 그래프
  graph[a].append(b)  

distance = [-1] * (n + 1)
distance[x] = 0

# bfs
q = deque([x])
while q:
  now = q.popleft()

  for next_node in graph[now]:
    if distance[next_node] == -1:  # 아직 방문하지 않은 노드이면
      distance[next_node] = distance[now] + 1
      q.append(next_node)

check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True

# 최단 거리가 k인 도시가 없다면
if check == False:
  print(-1)