def solution(land):
    
    for i in range(1, len(land)):
        for j in range(len(land[0])): 
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])  # 현재 열을 제외한 이전층에서의 최대값
        

    return max(land[len(land)-1])