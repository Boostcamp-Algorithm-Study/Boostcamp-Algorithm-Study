from collections import deque

def make_equal(arr1, arr2, sum_arr1, sum_arr2, target):
    cnt_arr1, cnt_arr2 = 0, 0
    length = len(arr1)
    
    op_cnt = 0
    while True:
        if op_cnt >= 3 * length: # 이 부분을 어떻게 설정하는가?
            op_cnt = -1
            break
        
        if sum_arr1 > target:
            cur = arr1.popleft()
            sum_arr1 -= cur
            cnt_arr1 += 1
            
            arr2.append(cur)
            sum_arr2 += cur
            op_cnt += 1
        else:
            cur = arr2.popleft()
            sum_arr2 -= cur
            cnt_arr2 += 1
            
            arr1.append(cur)
            sum_arr1 += cur
            op_cnt += 1
        
        if sum_arr1 == sum_arr2:
            break
    
    return op_cnt      
        

def solution(queue1, queue2):
    # pop 연산의 효율성을 위해 deque로 type casting
    queue1, queue2 = deque(queue1), deque(queue2)
    
    # 연산 효율성을 위해, 각 큐의 합계를 미리 계산
    sum_queue1, sum_queue2 = sum(queue1), sum(queue2)
    
    # target score 정의
    target_score = int((sum_queue1 + sum_queue2) / 2)
    
    # 알고리즘
    if sum_queue1 == sum_queue2:
        return 0
    else:
        answer = make_equal(queue1, queue2, sum_queue1, sum_queue2, target_score)
    
    return answer
