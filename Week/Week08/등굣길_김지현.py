def solution(m, n, puddles):
    
    padding = [0 for _ in range(m+1)]
    road = [padding] + [[0]+[1 for _ in range(m)] for _ in range(n)]
    
    for x,y in puddles : 
        road[y][x] = 0
        
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if i == 1 and j == 1 :
                continue
            
            if road[i][j] == 0:
                continue
            
            road[i][j] = road[i-1][j] + road[i][j-1]
            
    answer = road[n][m]%1000000007
    
    return answer
