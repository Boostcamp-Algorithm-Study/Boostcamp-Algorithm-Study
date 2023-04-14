def split_uv(p):
    l,r = 0,0
    for idx in range(len(p)):
        if p[idx] == '(':
            l += 1
        else :
            r += 1

        if l == r:
            u = p[:idx+1]
            v = p[idx+1:]
            return u, v
def correct(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True
        
def solution(p):
    answer = ''
    if p == '':
        return p
    
    u,v = split_uv(p)

    if correct(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ")"
        u = u[1:-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        
    return answer
