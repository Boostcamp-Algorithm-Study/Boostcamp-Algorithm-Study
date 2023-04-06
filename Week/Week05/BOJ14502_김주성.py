n, m = map(int, input().split()) 
data = []  # 초기 맵 리스트 
temp = [[0] * m for _ in range(n)]  # 벽이 추가된 맵 리스트 

for _ in range(n): 
  data.append(list(map(int, input().split()))) 

dx = [-1,  0, 1, 0] 
dy = [0, 1, 0, -1] 

result = 0 

def virus(x, y): 
  for i in range(4): 
    nx = x + dx[i] 
    ny = y + dy[i] 
    if nx >= 0 and nx < n and ny >= 0 and ny < m: 
      if temp[nx][ny] == 0:  # 빈공간 
        temp[nx][ny] = 2 
        virus(nx, ny) 

# 현재 temp 맵에서 안전 영역의 크기 계산 
def get_score(): 
  score = 0 
  for i in range(n): 
    for j in range(m): 
      if temp[i][j] == 0:  # 안전한 영역이라면 
        score += 1 
  return score  

def solution(count): 
  global result 

  # 울타리 3개가 설치된 경우 
  if count == 3: 
    for i in range(n): 
      for j in range(m): 
        temp[i][j] = data[i][j] 

    for i in range(n): 
      for j in range(m): 
        if temp[i][j] == 2: 
          virus(i, j) 

    result = max(result, get_score()) 
    return  

  # 울타리 설치 
  for i in range(n): 
    for j in range(m): 
      if data[i][j] == 0: 
        data[i][j] = 1 
        count += 1 
        solution(count)  
        data[i][j] = 0 
        count -= 1  

solution(0) 
print(result) 
