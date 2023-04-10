import sys
import heapq

# 프림 알고리즘 by chat-gpt
def prim(graph, start):
    answer = 0
    edges = [(weight, start, end) for end, weight in graph[start]]
    heapq.heapify(edges)
    visited = set([start])

    while edges:
        weight, start, end = heapq.heappop(edges)
        if end not in visited:
            answer += weight
            visited.add(end)

            for next_end, next_weight in graph[end]:
                if next_end not in visited:
                    heapq.heappush(edges, (next_weight, end, next_end))
        
        
    return answer
    

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    graph = {n:[] for n in range(1, n+1)}
    for _ in range(m):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    
    print(prim(graph, 1))
    