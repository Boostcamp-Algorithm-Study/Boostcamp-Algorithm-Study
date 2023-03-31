n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y):
  visited[y][x] = True
  color = graph[y][x]
  for dx, dy in d:
    X, Y = x + dx, y + dy
    if (0 <= X < n) and (0 <= Y < n):
      if visited[Y][X] == False and graph[Y][X] == color:
        dfs(X, Y)


a, b = 0, 0  # 정상, 적록색약 

for y in range(n):
  for x in range(n):
    if visited[y][x] == False:
      dfs(x, y)  
      a += 1

for y in range(n):
  for x in range(n):
    if graph[y][x] == 'G':
      graph[y][x] = 'R'

visited = [[False] * n for _ in range(n)]

for y in range(n):
  for x in range(n):
    if visited[y][x] == False:
      dfs(x, y)
      b += 1

print(a, b)
