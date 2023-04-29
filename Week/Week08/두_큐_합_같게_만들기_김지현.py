from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    sum1 = sum(queue1)
    
    queue2 = deque(queue2)
    sum2 = sum(queue2)
    
    # 예외 처리 
    # 전체 숫자의 합이 홀수인 경우
    if (sum1+sum2) % 2 == 1:
        return -1
    
    _max_iter = len(queue1) * 4
    while answer < _max_iter :
        if sum1 > sum2 :
            x = queue1.popleft()
            queue2.append(x)
            sum1 -= x
            sum2 += x
            answer += 1
        elif sum1 < sum2 :
            x = queue2.popleft()
            queue1.append(x)
            sum1 += x
            sum2 -= x
            answer += 1 
        else :
            break
        
    if answer == _max_iter :
        return -1
    
    return answer
