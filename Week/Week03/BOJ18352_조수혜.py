import sys
input = sys.stdin.readline
from collections import deque
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
# 거리 정보 입력 테이블 생성 후 초기화 
distance = [-1] * (N+1)

q = deque([X])

# 출발 위치는 0으로 설정
distance[X] = 0
    
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now]+1
            q.append(i)

cnt = 0
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        cnt += 1
        
if cnt == 0:
    print(-1) 
