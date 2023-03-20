# import
import heapq

# 입력
n,m = map(int, input("").split())

graph = [[] for _ in range(n+1)]
cows = [float('inf')] * (n+1)

for i in range(m) :
    a,b,c = map(int, input("").split())
    graph[a].append((c,b)) # (소, 헛간)로 저장
    graph[b].append((c,a))

# 시작 노드 설정
start = 1
cows[start] = 0
queue = []
heapq.heappush(queue, (0,start))

# 다익스트라 알고리즘
while queue :
    now_cow, now = heapq.heappop(queue)
    if now_cow > cows[now] :
        continue

    for node_cow, node in graph[now] :
        tmp = now_cow + node_cow
        if cows[node] > tmp :
            cows[node] = tmp
            heapq.heappush(queue, (cows[node], node))

# 정답 출력
print(cows[n])
