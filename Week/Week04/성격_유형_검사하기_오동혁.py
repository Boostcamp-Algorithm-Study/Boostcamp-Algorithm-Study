from collections import defaultdict


def solution(survey, choices):
    answer = [0]*4

    # 각 유형별 점수 저장하는 dictionary
    scores = defaultdict(int)
    # 유사 mbti, 각 유형별 자리
    mbti = {'RT': 0, 'CF': 1, 'JM': 2, 'AN': 3}

    # 점수를 확인해서 각 유형에 대한 점수 계산
    for s, c in zip(survey, choices):
        if c < 4:
            scores[s[0]] += 4-c
        else:
            scores[s[1]] += c-4

    # 각 유형별 자리에 대해서 점수를 확인한 뒤 무슨 유형인지 파악
    for k, v in mbti.items():
        if scores[k[0]] >= scores[k[1]]:
            answer[v] = k[0]
        else:
            answer[v] = k[1]

    return ''.join(answer)
