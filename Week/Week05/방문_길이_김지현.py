def solution(dirs) : 
    move_dict= {'R':0, 'L':1, 'U':2, "D":3}
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    visited_pairs = []

    count = 0
    prev = (0,0)

    for d in dirs :
        idx = move_dict[d]

        # 위치 이동 
        x,y = prev[0]+dx[idx], prev[1]+dy[idx]
        now = (x,y)

        # 이동한 위치(x,y)에 대한 검증 진행
        if -5<=x<=5 and -5<=y<=5:
            if prev < now: # (x,y,x',y')
                pair = prev + now 
            else :
                pair = now + prev
            
            if pair not in visited_pairs :
                count += 1
                visited_pairs.append(pair)

            prev = now

    return count
