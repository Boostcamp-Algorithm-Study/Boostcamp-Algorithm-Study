import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

# 배열을 벗어나는지 판단하는 함수


def pos(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False

# 새로 전파되는 바이러스 수를 세어주는 함수


def cnt_virus(case):
    # 초기 바이러스 수를 제외하고 새로 전파되는 바이러스의 수
    cnt = 0
    visit = set()

    for y, x in virus_area:
        dq = deque([(y, x)])
        visit.add((y, x))

        while dq:
            cy, cx = dq.popleft()

            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if pos(ny, nx) and lab[ny][nx] == 0 and not (ny, nx) in visit and not (ny, nx) in case:
                    visit.add((ny, nx))
                    dq.append((ny, nx))
                    cnt += 1

    return cnt


n, m = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(n)]
# 빈 칸을 저장해서 임의의 3개의 칸을 선택하도록 해줌
empty_area = []
# 초기 바이러스 위치를 저장
virus_area = []
# 안전 영역의 최대 크기
answer = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for y in range(n):
    for x in range(m):
        if lab[y][x] == 0:
            empty_area.append((y, x))
        elif lab[y][x] == 2:
            virus_area.append((y, x))

# 빈 칸중 3개의 임의의 칸을 선택한 경우의 수
cases = list(combinations(empty_area, 3))

# 각 경우마다 (빈 칸의 수 - 벽의 수(3) - 새로 전파된 바이러스 수)를 통해 안전영역의 크기를 구함
for case in cases:
    new_virus_cnt = cnt_virus(case)

    answer = max(answer, len(empty_area) - 3 - new_virus_cnt)

print(answer)
