def solution(land):
    prev = [0,0,0,0]
    
    for row in land :
        for i in range(4) :
            row[i] = max(prev[0:i]+prev[i+1:])+row[i]
        prev = row
        
    return max(land[-1])
