def solution(queue1, queue2):
    # 투포인터를 사용하기 위함
    q = queue1 + queue2
    
    if sum(q)%2 == 1:
        return -1
    else:
        # 목표값 설정
        total = sum(q) // 2
    
    # 큐 1을 기준으로 설정
    cnt, interval_sum = 0, sum(queue1)
    start, end = 0, len(queue1)-1
    
    while end < len(q) and start < len(q):
        if interval_sum == total:
            return cnt
        
        elif interval_sum < total and end < len(q)-1:
            end += 1
            interval_sum += q[end]
            
        else:
            interval_sum -= q[start]
            start += 1
            
        cnt += 1   
    
    return -1
