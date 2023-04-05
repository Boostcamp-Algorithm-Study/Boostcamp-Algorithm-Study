# Reference 1) https://hongcoding.tistory.com/130
# Reference 2) https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-14502-python-%EC%97%B0%EA%B5%AC%EC%86%8C
import sys, copy
from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(virus_pos):
    queue = deque(virus_pos)

    # 바이러스 퍼뜨리기
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (nx < 0) or (nx >= n) or (ny < 0) or (ny >= m):
                continue
            
            if tmp_graph[nx][ny] == 0:  # 빈 공간인 경우
                tmp_graph[nx][ny] = 2   # 바이러스가 퍼지고
                queue.append((nx, ny))  # 새 위치에서 다시 탐색한다
    
    # 안전영역 확인하기
    global answer   # 전역 변수를 최신화해야 함.
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:  # 바이러스가 퍼지지 않은 경우
                cnt += 1
    
    answer = max(answer, cnt)


if __name__ == "__main__":
    # 입력
    n, m = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    # 벽 설치가 가능한 위치와, 바이러스가 존재하는 위치를 미리 저장
    safe_area, virus = [], []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                safe_area.append((i, j))
            
            if graph[i][j] == 2:
                virus.append((i, j))

    # 벽 설치가 가능한 위치 중 3개를 뽑아서 설치한 뒤에, bfs를 호출한다.
    answer = 0
    for safe_points in combinations(safe_area, 3):
        tmp_graph = copy.deepcopy(graph)
        for x, y in safe_points:
            tmp_graph[x][y] = 1
        
        bfs(virus)
        
    print(answer)
