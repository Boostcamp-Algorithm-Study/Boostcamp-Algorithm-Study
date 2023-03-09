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

# 동작 흐름 (예제 1번)
"""
[(0, 2)]
-> [(1, 4), (1, 21)]
-> [(1, 21), (2, 8), (2, 41)]
-> [(2, 8), (2, 41), (2, 42)]
-> [(2, 41), (2, 42), (3, 16), (3, 81)]
-> [(2, 42), (3, 16), (3, 81), (3, 82)]
-> [(3, 16), (3, 81), (3, 82), (3, 84)]
-> [(3, 81), (3, 82), (3, 84), (4, 32), (4, 161)]
-> [(3, 82), (3, 84), (4, 32), (4, 161), (4, 162)]
-> [(3, 84), (4, 32), (4, 161), (4, 162)]
-> [(4, 32), (4, 161), (4, 162)]
-> [(4, 161), (4, 162), (5, 64)]
-> [(4, 162), (5, 64)]
-> 종료
"""