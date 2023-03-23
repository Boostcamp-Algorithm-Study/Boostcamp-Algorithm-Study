from itertools import permutations

def solution(k, dungeons) :
    answer, count, tired = 0, 0, k
    idxs_list = list(permutations(range(len(dungeons))))
    
    for idxs in idxs_list :
        for i in idxs :
            need, use = dungeons[i]
            if need > tired :
                continue
            tired -= use
            count += 1
            
        answer = max(answer, count)
        count, tired = 0, k
        
    return answer
