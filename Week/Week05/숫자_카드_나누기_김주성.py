import math 

def my_gcd(numbers): 
    result = numbers[0] 
    for i in range(1, len(numbers)):
        result = math.gcd(result, numbers[i])
    return result

def is_all_undivided(values, divisor): 
    for value in values: 
        if value % divisor == 0: 
            return False 
    return True 

def solution(arrayA, arrayB):
    
    answer = [1]
    
    case1 = my_gcd(arrayA) 
    case2 = my_gcd(arrayB)  
    
    if is_all_undivided(arrayB, case1): 
        answer.append(case1) 
    if is_all_undivided(arrayA, case2): 
        answer.append(case2) 
    
    return 0 if max(answer) == 1 else max(answer)