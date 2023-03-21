import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
INF = float('inf')

# 그래프 생성
graph = defaultdict(set)

# 입력을 받아서 단방향 그래프 초기화
for _ in range(m):
    start_node, end_node = map(int, input().split())

    graph[start_node].add(end_node)

# x 도시에서 각 도시까지 최단거리
dist = [INF]*(n+1)
# x 도시 값은 0으로 초기화
dist[x] = 0

# 다익스트라 이용
queue = [(0, x)]

while queue:
    cur_dist, cur_node = heapq.heappop(queue)

    for next_node in graph[cur_node]:
        next_dist = cur_dist + 1

        if next_dist < dist[next_node]:
            heapq.heappush(queue, (next_dist, next_node))
            dist[next_node] = next_dist

# 최단거리가 k인 도시가 있다면 True, 없다면 False
is_exist = False

for i in range(1, n+1):
    if dist[i] == k:
        is_exist = True
        print(i)

if not is_exist:
    print(-1)
