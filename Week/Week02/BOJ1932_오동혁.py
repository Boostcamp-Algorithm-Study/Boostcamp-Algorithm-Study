import sys

input = sys.stdin.readline

n = int(input())
# 정수 삼각혁
tr = [list(map(int, input().split())) for _ in range(n)]

# dynamic programming을 통해 해결
dp = [[0]*(i+1) for i in range(n)]
dp[0][0] = tr[0][0]

# 현재 칸에서 뻗어 나갈 수 있는 칸은 다음 줄(i+1)의 현재 인덱스(j) 또는 다음 인덱스(j+1)이다.
# 이를 통해 dp의 값을 최신화해 나감
for i in range(n-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + tr[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + tr[i+1][j+1])

print(max(dp[-1]))
