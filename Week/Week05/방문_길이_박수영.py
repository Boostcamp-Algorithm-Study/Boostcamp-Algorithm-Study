def solution(dirs):
    move = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    
    # 방문 처리용 집합
    visited = set()
    
    # 알고리즘
    start = (0, 0)
    for direction in dirs:
        nx, ny =  start[0] + move[direction][0], start[1] + move[direction][1]
        
        # 좌표평면을 벗어나는 경우, 예외처리
        if (nx < -5) or (nx > 5) or (ny < -5) or (ny > 5):
            continue
        
        road = ''.join([str(x)+str(y) for x, y in sorted([start, (nx, ny)], key=lambda x: (x[0], x[1]))])
        visited.add(road)
        start = (nx, ny)
        
    
    return len(visited)

if __name__ == "__main__":
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
    print(solution('UDUDUDUDUD'))