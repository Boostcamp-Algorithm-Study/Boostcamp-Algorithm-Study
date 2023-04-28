import heapq

def dijkstra(graph, start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        curr_distance, curr_node = heapq.heappop(heap)
        if curr_node in visited:
            continue
        visited.add(curr_node)

        for next_node, next_distance in graph[curr_node]:
            distance = curr_distance + next_distance

            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(heap, (distance, next_node))
    
    for idx in range(n + 1):
        if distances[idx] == float('inf'):
            distances[idx] = 0
            
    return distances[1:]


if __name__ == "__main__":
    from collections import defaultdict
    import sys

    # 입력
    n = int(input())
    m = int(input())

    graph = defaultdict(list)
    for _ in range(m):
        start, arrive, weight = map(int, sys.stdin.readline().split())
        graph[start].append((arrive, weight))
    
    # 알고리즘
    result = []
    for city in range(1, n+1):
        result.append(dijkstra(graph, city))

    for line in result:
        print(*line)
    