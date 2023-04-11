def solution(dirs):
  answer = 0
  x, y = 5, 5
  
  visited = set()

  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  move_types = ['R', 'D', 'L', 'U']

  for d in dirs:
    for i in range(4):
      if d == move_types[i]:
        nx = x + dx[i]
        ny = y + dy[i]
    if nx < 0 or ny < 0 or nx > 10 or ny > 10:
      continue

    if (x, y, nx, ny) not in visited:
      answer += 1
      visited.add((x, y, nx, ny))
      visited.add((nx, ny, x, y))
      # print(visited)

    x, y = nx, ny

  return answer