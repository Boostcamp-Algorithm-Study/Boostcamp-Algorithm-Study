import numpy as np
from itertools import product
def solution(user_id, banned_id):
    answer = []
    for id in banned_id:
        
        # "*"처리된 인덱스를 담을 리스트 선언
        star = []
        # 불량 아이디와 같을 수 있는 아이디를 담을 리스트 선언
        ids = []
        for i,x in enumerate(id):
            if x == '*':
                star.append(i)
        
        for u_id in user_id:
            if len(u_id) == len(id):
                new_id = u_id
                for s in star:
                    # "*"위치 인덱스를 '*'로 변경
                    new_id = new_id[:s] + '*'+ new_id[s+1:]
                # ID가 불량 ID와 같으면 리스트에 추가 
                if new_id == id:
                    ids.append(u_id)
                    
        answer.append(ids)
    
    # 중복 순열
    answer = list(product(*answer))
    # 리스트 내 정렬
    answer = [sorted(x) for x in answer if len(x) == len(set(x))]
    # 중복제거
    answer = set(list(map(tuple,answer)))
    
    return len(answer)
