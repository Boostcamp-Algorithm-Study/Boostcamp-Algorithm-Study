# import
from collections import deque
from itertools import combinations
from copy import deepcopy

# input
N, M = map(int,input('').split())
maps, blanks, viruses = [], [], []

for i in range(N) :
    inputs = list(map(int,input('').split()))
    for j, value in enumerate(inputs) :
        if value == 1 : # wall
            continue
        if value == 0 :
            blanks.append((i,j))
        elif value == 2 :
            viruses.append((i,j))

    maps.append(inputs)

# bfs
def bfs(start,visited,modified_maps) :
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    queue = deque([start])

    while queue :
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4) :
            sx,sy = x+dx[i], y+dy[i]
            if sx>=0 and sx<N and sy>=0 and sy<M :
                if modified_maps[sx][sy]==0 and not visited[sx][sy] :
                    queue.append((sx,sy))
                    visited[sx][sy] = True
                    modified_maps[sx][sy] = 2        

    return modified_maps, visited
    
# run
safe = 0
for blank in combinations(blanks,3) :
    modified_maps = deepcopy(maps)
    for (blank_x, blank_y) in blank:
        modified_maps[blank_x][blank_y] = 1

    visited = [[False] * M for _ in range(N)]
    for virus in viruses :
        virus_x, virus_y = virus
        if not visited[virus_x][virus_y] :
            modified_maps, visited = bfs(virus, visited, modified_maps)

    count = 0
    for row in modified_maps:
        count += row.count(0)

    safe = max(safe, count)

# output
print(safe)
    
