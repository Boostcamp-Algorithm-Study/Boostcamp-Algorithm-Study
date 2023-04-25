import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

cost = [[float('inf')]*n for _ in range(n)]

# 각 정류장에서 다른 모든 정류장까지의 비용 최솟값을 구해야되기 때문에 플로이드-워셜 알고리즘 사용
for _ in range(m):
    start, end, c = map(int, input().split())

    cost[start-1][end-1] = min(cost[start-1][end-1], c)

for mid in range(n):
    for start in range(n):
        for end in range(n):
            cost[start][end] = min(
                cost[start][end], cost[start][mid] + cost[mid][end])

for i in range(n):
    for j in range(n):
        if cost[i][j] == float('inf') or i == j:
            cost[i][j] = 0
    print(*cost[i])
