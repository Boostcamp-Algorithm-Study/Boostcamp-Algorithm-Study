def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    # 알고리즘
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == 1:
                continue
            
            # TODO : 웅덩이인 경우 무시
            if [j, i] in puddles:
                continue
            # TODO : 웅덩이가 아닌 경우 기록
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
       
    return dp[-1][-1]

# print(solution(4, 3, [[2, 2], [3, 2]]))