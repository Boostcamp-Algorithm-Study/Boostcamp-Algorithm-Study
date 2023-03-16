n, k = map(int, input().split())

bag = []
for _ in range(n):
    bag.append(list(map(int, input().split())))

# 최대 무게 + 1 만큼 0으로 채운 2차원 리스트 생성    
dp = [[0]*(k+1) for _ in range(n+1)]

# 가방 개수 만큼 반복
for i in range(n):
    # 첫번쨰 인자는 무게, 두번째 인자는 가치
    weight, value = bag[i][0], bag[i][1]
    
    
    for j in range(1,k+1):
        # 배낭에 물건을 넣을 수  있으면 비교
        if j >= weight:
            # 현재 넣을 물건의 무게만큼 배낭에서 뺴고, 현 물건을 넣었을때의 가치 / 현재 물건을 넣지 않고 그대로의 가치 비교 후  갱신
            dp[i+1][j] = max(dp[i][j], dp[i][j-weight] + value)
            
        else:
            dp[i+1][j] = dp[i][j]

print(dp[n][k])
