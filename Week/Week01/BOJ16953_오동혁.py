import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def solution(a, b, cur):
    global ans

    if a == b:
        ans = min(ans, cur)
        return
    elif a > b:
        return

    solution(a*2, b, cur+1)
    solution(a*10 + 1, b, cur+1)


a, b = map(int, input().split())

ans = float('inf')

solution(a, b, 1)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
