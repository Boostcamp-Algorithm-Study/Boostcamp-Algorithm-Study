from collections import deque
N = int(input())

arr = list(map(int, input().split()))
M = int(input())

# 입력받은 list를 graph형식으로 변환
graph = [[] for _ in range(N+1)]
for idx, x in enumerate(arr):
    if x != -1:
        graph[x].append(idx)


def bfs(start):
    arr[start] = -2
    q = deque()
    q.append(start)
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            # 삭제해야하는 노드는 -2로 변환
            if arr[i] != -2:
                arr[i] = -2
                q.append(i)

bfs(M)

cnt = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        cnt += 1
print(cnt)
