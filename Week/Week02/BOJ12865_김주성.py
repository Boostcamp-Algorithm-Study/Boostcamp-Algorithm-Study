N, K = map(int, input().split())  # 물건 수, 최대 무게 
stuff = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    stuff.append((W, V))
    
dp = [[0]*(K+1) for _ in range(N+1)]

for step in range(1, N+1):
    w, v = stuff[step]
    for curr_w in range(1, K+1):  
        if curr_w <= w:  # 물건이 들어갈 수 없는 경우 
            dp[step][curr_w] = dp[step-1][curr_w] 
        else:
        	# 현재 물건을 넣지 않았을 때, 넣었을 때 
            dp[step][curr_w] = max(dp[step-1][curr_w], dp[step-1][curr_w-w] + v)

print(dp[N][K])