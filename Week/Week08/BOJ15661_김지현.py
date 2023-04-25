# 15661 링크와 스타트
# 문제 조건 : 인원은 달라도 되지만 한명 이상이어야 한다.
from itertools import combinations

# 팀의 능력치 계산 Fn.
def calculate(power, team) :
    score = 0
    team = list(team)
    for idx, person in enumerate(team) :
        for other in team[idx:]:
            score += (power[person][other] + power[other][person])
    return score

# main
N = int(input())
power = []
for _ in range(N) :
    power.append(list(map(int, input().split())))

min_diff = float('inf')
for people in range(1,N//2+1) :
    for start_team in combinations(range(N), people) :
        link_team = list(set(range(N))-set(start_team))
        start_score, link_score = calculate(power,start_team), calculate(power,link_team)
        diff = abs(start_score-link_score)
        min_diff = min(diff, min_diff)

print(min_diff)    
