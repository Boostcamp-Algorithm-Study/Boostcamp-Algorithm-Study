def solution(queue1, queue2):
    cnt = 0

    # 각 queue의 원소 합을 미리 구함
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    
    # 두 개의 queue합이 홀수라면 원소 합을 같게 만들 수 없음
    if (q1_sum + q2_sum) % 2:
        return -1
    
    # 목표로 해야되는 각 큐의 원소 합
    target = (q1_sum + q2_sum) // 2
    
    # 두 개의 큐를 하나로 만듦 -> 투 포인터로 문제 해결
    queue = queue1 + queue2
    # 투 포인터의 초기 값은 0, 처음 주어진 두 큐의 길이 - 1 (인덱스 값이기 때문)
    start, end = 0, len(queue) // 2 - 1
    # 투 포인터 사이의 원소 합
    start_end_sum = sum(queue[start:end+1])

    # 투 포인터 사이의 원소 합이 target과 같아질 때까지 반복
    while start_end_sum != target:
        if start_end_sum < target:
            end += 1
            # end가 범위를 벗어나면 원소 합을 같게 만들 수 없음
            if end == len(queue):
                return -1
            start_end_sum += queue[end]
        else:
            start_end_sum -= queue[start]
            start += 1

        cnt += 1
    
    return cnt