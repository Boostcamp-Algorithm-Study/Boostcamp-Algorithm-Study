def solution(n):
    
    answer = []
    while 0 < n:
        if n % 3 != 0: 
            answer.append(str(n % 3))  # 1, 2 
            n = n // 3 
        else:  
            answer.append('4')  # 4 
            n = n // 3 - 1  
            
    answer = ''.join(answer[::-1])
    return answer