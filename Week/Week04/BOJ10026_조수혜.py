import sys
sys.setrecursionlimit(1000000)

N = int(input())

array = []
for _ in range(N):
    array.append(list(input().rstrip()))
    
visited = [[False] * N for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited[x][y] = True
    color = array[x][y]
    
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        
        if (0<= new_x < N) and (0 <= new_y < N):
            if visited[new_x][new_y] == False and array[new_x][new_y] == color:
                dfs(new_x, new_y)

cnt1, cnt2 = 0,0

# 색맹이 아닌 경우
for x in range(N):
    for y in range(N):
        if visited[x][y] == False:
            dfs(x,y)
            cnt1 += 1
            
# 색맹인 경우 - visited 초기화
visited = [[False] * N for _ in range(N)]

# G-> R로 바꿔줌
for i in range(N):
    for j in range(N):
        if array[i][j] == 'G':
            array[i][j] = 'R'
    
for x in range(N):
    for y in range(N):
        if visited[x][y] == False:
            dfs(x,y)
            cnt2 += 1

print(cnt1, cnt2)
