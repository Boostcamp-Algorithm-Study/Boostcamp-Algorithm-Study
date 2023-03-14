def solution(routes):

    result = 0 
    routes.sort(key=lambda x: x[1]) 

    camera = -30001 
    for route in routes: 
        if camera < route[0]: 
            result += 1 
            camera = route[1]  
    
    return result 

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
