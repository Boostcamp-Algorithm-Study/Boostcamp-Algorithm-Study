import sys
import heapq
from collections import defaultdict # N, M 값을 보니깐 매번 확인하는 조건을 걸면 시간 초과날 것 같음

# 다익스트라 알고리즘
def dijkstra(graph: dict, start: int):
    distances = {node: float('inf') for node in range(1, n+1)}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph[current_node]:
            distance = current_distance + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# 알고리즘
if __name__ == '__main__':
    # 입력
    n, m, k, x = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
    
    # print(graph)

    distance_dict = dijkstra(graph, x)
    distance_list = sorted(distance_dict.items(), key=lambda x: x[0])

    cnt = 0
    for num_city, distance in distance_list:
        if distance == k:
            cnt += 1
            print(num_city)

    if cnt == 0:
        print(-1)
