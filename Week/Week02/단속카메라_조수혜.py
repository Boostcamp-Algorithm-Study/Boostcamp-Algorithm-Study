def solution(routes):
    answer = 0
    routes.sort(key=lambda x:(x[1],x[0]))
    a = -30001
    for route in routes:
        if a < route[0]:
            answer += 1
            a = route[1]
    return answer
