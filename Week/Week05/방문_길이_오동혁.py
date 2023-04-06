def solution(dirs):
    answer = 0
    dir_dict = {'U': 0, 'L': 1, 'D': 2, 'R': 3}
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    visit = [[[False]*4 for _ in range(11)] for _ in range(11)]
    y, x = 0, 0

    for d in dirs:
        ny = y + dy[dir_dict[d]]
        nx = x + dx[dir_dict[d]]

        if -5 <= ny <= 5 and -5 <= nx <= 5:
            if not visit[y+5][x+5][dir_dict[d]]:
                visit[y+5][x+5][dir_dict[d]] = True
                visit[ny+5][nx+5][(dir_dict[d]+2) % 4] = True
                answer += 1

            y, x = ny, nx

    return answer
