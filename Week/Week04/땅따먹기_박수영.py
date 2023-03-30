# time: 54m

def solution(land):
    answer = 0
    
    dp = land[0]
    for i in range(1, len(land)):
        pos_0 = max([land[i][0] + dp[j] for j in range(4) if j != 0])
        pos_1 = max([land[i][1] + dp[j] for j in range(4) if j != 1])
        pos_2 = max([land[i][2] + dp[j] for j in range(4) if j != 2])
        pos_3 = max([land[i][3] + dp[j] for j in range(4) if j != 3])
        
        dp = [pos_0, pos_1, pos_2, pos_3]
    
    answer = max(dp)
    return answer

if __name__ == '__main__':
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))