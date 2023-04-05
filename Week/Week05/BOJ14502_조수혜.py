from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
    
# 바이러스가 퍼지지 않은 곳
zeros = []

# 바이러스가 퍼진 곳
virus = []

# 배열을 돌면서 바이러스가 퍼진 곳과 퍼지지 않은 곳의 공간 정보를 담아줌
for x in range(N):
    for y in range(M):
        if arr[x][y] == 0:
            zeros.append([x,y])
        elif arr[x][y] == 2:
            virus.append([x,y])


dx = [-1,1,0,0]
dy = [0,0,-1,1]

res = 0     

# BFS (바이러스를 퍼트림)
def bfs():
    global res
    cnt = len(zeros) - 3    # 현재 배열에서의 안전한 구역 카운트 (벽을 3개 세워야 함)
    q = deque()
    for x, y in virus:
        q.append((x,y))
        
    while q:
        x1, y1 = q.popleft()
        
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            
            if 0<=nx<N and 0<=ny<M and new_arr[nx][ny] == 0:
                new_arr[nx][ny] = 2
                q.append([nx, ny])
                cnt -= 1
    res = max(cnt, res)

       
    
# 벽을 세울 수 있는 조합
for com in combinations(zeros, 3):
    new_arr = deepcopy(arr)
    
    for x, y in com:
        new_arr[x][y] = 1
    bfs()
    
print(res)
