from collections import deque 

# bfs
def bfs(n, map, visited, start) :
    dx,dy = [1,-1,0,0], [0,0,1,-1]
    queue = deque([start])

    while queue :
        x,y = queue.popleft()
        visited[x][y] = True
        color = map[x][y]

        for i in range(4) :
            sx, sy = x+dx[i], y+dy[i]
            if sx>=0 and sx<n and sy>=0 and sy<n and color == map[sx][sy]:
                if not visited[sx][sy] :
                    queue.append((sx, sy))
                    visited[sx][sy] = True
    
    return color, visited

# 입력
n = int(input(""))

map = []
for _ in range(n) :
    map.append(list(input("")))

# 적록 색약이 아닌 사람
rgb_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            color, visited = bfs(n,map,visited,(i,j))
            rgb_count += 1

# 적록 색약인 사람
for i in range(n) :
    for j in range(n) :
        if map[i][j] == 'G' :
            map[i][j] = 'R'

rb_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            color, visited = bfs(n,map,visited,(i,j))
            rb_count += 1

# 출력
print(rgb_count, rb_count)
