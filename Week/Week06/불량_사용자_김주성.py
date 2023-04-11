from itertools import permutations 

def check(candidates, banned_id):  # 하나라도 매핑이 되지 않으면 False 리턴 
    for i in range(len(banned_id)): 
        if len(candidates[i]) != len(banned_id[i]): 
            return False 
        for a, b in zip(candidates[i], banned_id[i]): # 문자열을 돌며
            if b == '*': 
                continue 
            if a != b: 
                return False 
    return True 

def solution(user_id, banned_id):
    answer = [] 
    
    for candidates in permutations(user_id, len(banned_id)):  # 모든 경우를 고려 
        if check(candidates, banned_id):  # candidate와 banned_id가 매핑이 되는지
            candidates = set(candidates)  # 후보들 사이의 순서 정보를 없애기 위해
            if candidates not in answer:  
                answer.append(candidates) # 현재 경우를 추가 
    return len(answer) 

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))