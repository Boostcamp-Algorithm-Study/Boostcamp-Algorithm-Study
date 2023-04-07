def solution(dirs):
    answer = []
    moving = {'L':[-1,0], 'R':[1,0], 'U':[0,1], 'D':[0,-1]}
    x,y = 0,0
    for d in dirs:
        dx, dy = moving[d][0], moving[d][1]
        if abs(x+dx) <= 5 and abs(y+dy) <= 5:
            answer.append((dx+x,dy+y,x,y))
            answer.append((x,y,dx+x,dy+y))
            x = x+dx
            y = y+dy
    return len(set(answer))//2 
