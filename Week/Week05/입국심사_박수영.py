def solution(n, times):
    answer = 0
    times.sort()
    lb, ub = 1, times[0] * n
    
    while True:
        center = (lb + ub) // 2
        
        if lb == center: # 더 이상 업데이트되지 않는 경우
            answer = (center + 1)
            break
        
        cnts = []
        for time in times:
            cnts += [center // time]
        
        if sum(cnts) < n: # 시간을 늘려야 함
            lb = center
        elif sum(cnts) > n: # 시간을 줄여야 함
            ub = center
        else:
            tmp = float('-inf')
            
            for time, cnt in zip(times, cnts):
                tmp = max(tmp, time*cnt)
            
            answer = tmp
            break
            
    return answer

if __name__ == '__main__':
    print(solution(6, [7, 10]))
    print(solution(10, [6, 8, 10]))