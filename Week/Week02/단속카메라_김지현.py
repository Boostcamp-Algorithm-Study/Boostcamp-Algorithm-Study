def solution(routes):
    routes = sorted(routes, key = lambda x : x[1])
    times = [[-30000,30000]]
    
    for i in range(len(routes)) :
        for t in range(len(times)) :
            if routes[i][0] <= times[t][1] :
                times[t] = [routes[i][0], min(times[t][1], routes[i][1])]
                break
        else :
            times.append(routes[i])
    
    return len(times)
