def solution(number, k):
    answer = [] 
    for num in number: 
        if len(answer) == 0: 
            answer.append(num) 
            continue 
        
        while answer[-1] < num and k > 0: 
            answer.pop()  # num보다 작은 수는 제거 
            k -= 1 
            if len(answer) == 0 or k <= 0: 
                break 

        answer.append(num)  # answer에는 num 보다 큰 수만 쌓일 수 있도록   
        

    answer = answer[:-k] if k > 0 else answer 
    return ''.join(answer) 

print(solution("1231234", 3))