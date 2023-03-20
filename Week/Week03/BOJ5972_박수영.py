import sys, heapq

# 다익스트라 알고리즘 by ChatGPT
def dijkstra(graph: dict, start: int):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)    # 최소 힙이 default이므로, 가장 거리가 짧은 heap을 추출
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))  # 거리 순으로 min-heap이 만들어짐

    return distances

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    graph = {}  # 그래프 만들기
    for _ in range(M):
        root_node, dest_node, weight = map(int, sys.stdin.readline().split())

        if root_node in graph.keys():
            if (dest_node in graph[root_node].keys()):
                if weight < graph[root_node][dest_node]:
                    graph[root_node][dest_node] = weight
            else:
                graph[root_node].update({dest_node:weight})
        else:
            graph[root_node] = {dest_node:weight}
        
        if dest_node in graph.keys():
            if (root_node in graph[dest_node].keys()):
                if weight < graph[dest_node][root_node]:
                    graph[dest_node][root_node] = weight
            else:
                graph[dest_node].update({root_node:weight})
        else:
            graph[dest_node] = {root_node:weight}
        
    # import pprint
    # pprint.pprint(graph)

    distances = dijkstra(graph, 1)
    print(distances[N])
