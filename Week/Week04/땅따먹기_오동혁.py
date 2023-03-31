def solution(land):
    cur_answer = land[0]

    for i in range(1, len(land)):
        temp = [0]*4
        for j in range(4):
            temp[j] = land[i][j] + max(cur_answer[:j] + cur_answer[j+1:])
        cur_answer = temp[:]

    return max(cur_answer)
