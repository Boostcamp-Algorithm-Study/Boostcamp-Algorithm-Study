# 단위를 증가시키면서 잘라나간다
# 단위 별 등장 횟수를 저장해둔다
# 저장한 값으로 문자열을 압축하고, 비교한다.

def solution(s):
    answer = float('inf')
    
    unit = 1
    counts = []
    while unit <= len(s):
        for start in range(0, len(s), unit):
            curr = s[start:start+unit]
            if start == 0:
                counts.append([1, curr])
                continue
            
            if curr == counts[-1][1]:
                counts[-1][0] += 1
            else:
                counts.append([1, curr])
        
        candidate = ''.join([str(num)+ch if num > 1 else ch for num, ch in counts])
        answer = min(answer, len(candidate))
        counts = []
        unit += 1   
    
    
    return answer


if __name__ == "__main__":
    print(solution("aabbaccc")) # 7
    print(solution("ababcdcdababcdcd")) # 9
    print(solution("abcabcdede")) # 8
    print(solution("abcabcabcabcdededededede")) # 14
    print(solution("xababcdcdababcdcd")) # 17