# 균형잡힌 괄호 문자열의 인덱스 반환 
def balanced_index(p): 
    count = 0  # 왼쪽 괄호의 개수 
    for i in range(len(p)): 
        if p[i] == '(': 
            count += 1 
        else: 
            count -= 1 
        if count == 0:  # 균형이 맞는 순간
            return i 

# 올바른 괄호문자열인지 판단 (균형 잡힌 문자열은 보장)
def check_proper(p): 
    count = 0  # 왼쪽 괄호의 개수 
    for i in p: 
        if i == '(':  # 올바른 괄호 문자열이라면 여는 괄호로 시작 
            count += 1 
        else: 
            if count == 0:  # 쌍이 맞지 않는 경우
                return False    
            count -= 1 
    return True
        

def solution(p):
    answer = ''
    if p == '': 
        return answer 
    
    index = balanced_index(p) 
    u = p[:index+1]  # 균형잡힌 괄호 문자열 
    v = p[index+1:]  
    
    if check_proper(u): 
        answer = u + solution(v) 
    else: 
        answer = '(' 
        answer += solution(v) 
        answer += ')' 
        u = list(u[1:-1]) 
        for i in range(len(u)): 
            if u[i] == '(': 
                u[i] = ')'
            else: 
                u[i] = '(' 
        
        answer += ''.join(u) 
    return answer 