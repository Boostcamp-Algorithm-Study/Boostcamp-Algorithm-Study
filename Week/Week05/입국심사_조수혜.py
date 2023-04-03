def solution(n, times):
    times.sort()
    answer = 0
    min_t, max_t = times[0], times[-1] * n  # 가장 오래걸리는 심사관에게 모두 심사받는 경우
    while min_t <= max_t:
        mid_t = (max_t+min_t) //2
        cnt = 0
        
        for time in times:
            # 모든 심사관이 mid time만큼 심사한 사람 수
            cnt += mid_t//time
            # 사람수 보다 같거나 많으면 반복문 탈출
            if cnt >= n:
                break
        
        # 심사한 사람이 n 보다 같거나 많은 경우
        if cnt >= n:
            answer = mid_t
            max_t = mid_t -1
        else:
            min_t = mid_t +1  
        
    return answer
