def solution(survey, choices):
    idxs = {'R':0, 'T':0, 'C':1, 'F':1, 'J':2, 'M':2, 'A':3, 'N':3}
    results = [{'R':0,'T':0},{'C':0,'F':0},{'J':0,'M':0},{'A':0,'N':0}]
    
    for strs, choice in zip(survey, choices) :
        char = strs[choice//4]
        score = choice%4 if choice//4 == 1 else 4-choice
        results[idxs[char]][char] += score
    
    answer = ""
    for result in results :
        value = list(result.values())
        key = result.keys()

        if value[0] == value[1] :
            answer += min(key)
        else :
            answer += max(key, key=lambda x : result[x])
        
    return answer
