from itertools import permutations
import re

def solution(user_id, banned_id):
    users = []
    permutation_list = list(permutations(user_id, len(banned_id)))
    for permute_banned_id in permutation_list :
        fail = False
        for ori, permute in zip(banned_id, permute_banned_id) :
            if set(permute_banned_id) in users :
                fail = True
                continue
                
            regex_ori = re.compile(ori.replace('*','[0-9a-z]{1}'))
            if not re.fullmatch(regex_ori, permute) :
                fail = True
                break

        if not fail:
            users.append(set(permute_banned_id))
            
    return len(users)
