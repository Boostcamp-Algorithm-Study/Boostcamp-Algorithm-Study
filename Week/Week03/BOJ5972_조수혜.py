import heapq

# N개의 헛간, M개의 길 입력
N, M = map(int, input().split())
INF = int(1e9)

# 길을 찾기 위한 2차원 리스트 생성
graph = [[] for _ in range(N+1)]

# M개의 길 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1)

# 다익스트라 함수 
def find_root(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    distance[start] = 0
    heapq.heappush(q, (0,start))
    
    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
                
        # 현재 노드가 이미 처리된 적이 있는  노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접 노드 확인
        for next_dist, next_cost in graph[now]:
            cost = dist + next_cost
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_dist]:
                distance[next_dist] = cost
                heapq.heappush(q, (cost, next_dist))


find_root(1)
print(distance[-1])     
