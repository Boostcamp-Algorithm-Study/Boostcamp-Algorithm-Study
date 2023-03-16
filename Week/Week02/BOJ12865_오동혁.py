import sys
import copy

input = sys.stdin.readline

n, k = map(int, input().split())

baggages = [list(map(int, input().split())) for _ in range(n)]

# 최종 결과 dp 배열
dp = [0]*(k+1)
# 물건 1개를 계산할 때마다 최신화한 dp 배열
temp_dp = [0]*(k+1)

visit_w = {0}

for w, v in baggages:
    temp_set = set()

    for t in visit_w:
        if t+w <= k:
            temp_dp[t+w] = max(dp[t+w], dp[t]+v)
            temp_set.add(t+w)

    dp = copy.deepcopy(temp_dp)
    visit_w = visit_w.union(temp_set)

print(max(dp))
