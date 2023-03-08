import sys
from collections import deque

# 입력부
a, b = map(int, sys.stdin.readline().strip().split())

# 알고리즘
answer = -1

candidate = deque([(0, a)])
while candidate:
    cnt, cur = candidate.popleft()
    if cur == b:
        answer = cnt + 1
        break
    
    case_1, case_2 = cur*2, int(str(cur) + '1')
    if case_1 <= b:
        candidate.append((cnt+1, case_1))
    
    if case_2 <= b:
        candidate.append((cnt+1, case_2))

print(answer)
