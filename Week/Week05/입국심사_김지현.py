def solution(n, times):

    left, right = min(times), min(times)*n
    
    while left <= right : 
        people = 0 
        mid = (left+right)//2
        
        # 특정 시간 동안 심사관이 심사할 수 있는 인원 계산
        for time in times :
            people += mid//time
        
        # n명을 심사하는데 드는 최소 시간 탐색
        if people < n : 
            left = mid+1
        else :
            answer = mid
            right = mid-1
    
    return answer
