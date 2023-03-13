from collections import deque
import copy

def solution(routes):
    routes = deque(sorted(routes, key=lambda x: x[1]))
    # print(routes)
    
    answer = 0
    while routes:
        cur_enter, cur_exit = routes.popleft()   
        tmp = copy.deepcopy(routes)
        for enter, exit in tmp:
            if ((cur_enter <= enter) and (enter <= cur_exit)) or ((enter <= cur_enter) and (cur_enter <= exit)):
                routes.popleft()
            else:
                break
            
        answer += 1
    
    return answer
