from itertools import permutations
def solution(k, dungeons):
    answer = -1
    per = list(permutations(dungeons,len(dungeons)))
    
    for i in per:
        a = k
        num = 0
        for j in i:
            if j[0] <= a:
                a -= j[1]
                num += 1
        answer = max(answer,num)
    return answer
