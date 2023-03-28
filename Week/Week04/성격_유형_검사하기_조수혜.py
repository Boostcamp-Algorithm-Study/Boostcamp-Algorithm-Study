def solution(survey, choices):
    answer = ''
    # 점수 저장을 위한 딕셔너리 생성
    jipo = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0,'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        l = survey[i][0]
        r = survey[i][1]
        
        # 점수가 5점 이상일때
        if choices[i] -4 > 0:
            jipo[r] += choices[i]-4
        
        # 점수가 3점 이하일때
        elif choices[i] - 4 < 0:
            jipo[l] += 4-choices[i]
            
    # 둘 중 더 높은 점수를 최종 반환
    answer += 'R' if jipo['R'] >= jipo['T'] else 'T'
    answer += "C" if jipo['C'] >= jipo['F'] else 'F'
    answer += 'J' if jipo['J'] >= jipo['M'] else 'M'
    answer += 'A' if jipo['A'] >= jipo['N'] else 'N'
    return answer
