# 18352
# import
from collections import deque

# 입력 (도시, 도로, 거리정보, 출발도시번호)
n,m,k,x = map(int, input("").split())

graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
visited = [False] * (n+1)

for i in range(m) :
    a,b = map(int,input('').split())
    graph[a].append(b)

# bfs
queue = deque([x])
distance[x] = 0
visited[x] = True

while queue :
    v = queue.popleft()
    for i in graph[v] :
        if not visited[i]: 
            visited[i] = True
            distance[i] = distance[v] + 1
            queue.append(i)

# 정답 출력
not_answer = True
for idx, value in enumerate(distance) :
    if value == k :
        no_answer = False
        print(idx)

if not_answer :
    print(-1)
