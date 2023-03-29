def solution(s):
    answer = 1001
    if len(s) == 1:
        return 1
    
    for i in range(1,len(s)//2+1):
        # 최종 문자열, 현재 단위 문자열 선언
        new_s, tmp = '', ''
        # 현재 단위 문자열이 반복된 횟수
        cnt = 1

        for j in range(len(s)//i+1):
            # 다음 단위 문자열과 비교
            if tmp == s[j*i:j*i+i]:
                cnt += 1
            else:
                if cnt > 1:
                    new_s += str(cnt) + tmp
                else:
                    new_s += tmp
                cnt = 1
                tmp = s[j*i:j*i+i]
        new_s += tmp
        answer = min(len(new_s), answer)
    return answer
