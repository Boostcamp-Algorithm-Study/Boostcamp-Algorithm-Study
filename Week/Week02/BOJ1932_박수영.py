import sys

# 입력부
n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

# 알고리즘
dp = [triangle[0]]
for level, t in enumerate(triangle[1:], start=1):
    tmp = []

    for idx, val in enumerate(t):
        if idx == 0:
            tmp.append(val + dp[level-1][idx])
        elif idx == (len(t) - 1):
            tmp.append(val + dp[level-1][idx-1])
        else:
            tmp.append(val + max(dp[level-1][idx], dp[level-1][idx-1]))
    
    dp.append(tmp)

print(max(dp[-1]))
