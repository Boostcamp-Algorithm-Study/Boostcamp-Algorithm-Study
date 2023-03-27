# time: 25m

def solution(survey, choices):
    # 성격 유형별 점수를 저장하는 곳이 필요.
    scores = {ch_type:0 for ch_type in "RTCFJMAN"}
    
    # survey와 choices는 같은 길이의 배열이므로, zip을 활용할 수 있을 듯
    for (disagree, agree), choice in zip(survey, choices):
        if choice > 4:
            scores[agree] += (choice - 4)
        elif choice < 4:
            scores[disagree] += (4 - choice)
    
    # 점수가 높은 순으로 정렬하되, 같은 경우 사전순으로 반환
    answer = ''
    tmp = []
    for idx, scores in enumerate(scores.items()):
        tmp.append(scores)
        
        if (idx % 2):
            tmp.sort(reverse=True, key=lambda x: (x[-1], -ord(x[0])))
            answer += tmp[0][0]
            tmp = []
    
    return answer

if __name__ == "__main__":
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))
    