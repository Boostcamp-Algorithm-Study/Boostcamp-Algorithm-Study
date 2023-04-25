import sys

input = sys.stdin.readline

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')

# 모든 조합을 구함
# 2진법을 활용해 1이 존재하는 자리의 사람 번호가 한팀
for i in range(1, 2**(n-1)):
    # num1 & num2 = 0이 되도록 만들어줌 -> 양 팀에 모두 속하는 사람이 존재하지 않고, 모든 사람들이 참여
    num1 = i
    num2 = 2**n - i - 1

    team1 = []
    team2 = []
    team1_sum = 0
    team2_sum = 0

    # 같은 팀인 사람을 각 list에 넣어줌
    for j in range(n):
        if num1 & (1 << j):
            team1.append(j)

        if num2 & (1 << j):
            team2.append(j)

    # 각 팀의 능력치를 구해줌
    for p1_idx in range(len(team1)):
        for p2_idx in range(p1_idx, len(team1)):
            team1_sum += ability[p1_idx][p2_idx] + ability[p2_idx][p1_idx]

    for p1_idx in range(len(team2)):
        for p2_idx in range(p1_idx, len(team2)):
            team2_sum += ability[p1_idx][p2_idx] + ability[p2_idx][p1_idx]

    answer = min(answer, abs(team1_sum - team2_sum))

print(answer)
