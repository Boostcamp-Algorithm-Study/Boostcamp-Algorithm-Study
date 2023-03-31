def solution(land):

    for i in range(1,len(land)):
        for j in range(4):
            land[i][j] += max([land[i-1][x] for x in range(4) if x!= j])

    return max(land[-1])
