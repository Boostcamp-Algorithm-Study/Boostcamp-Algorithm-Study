def right(x):
    stack = []
    for i in x :
        if i == "(" :
            stack.append("(")
        else :
            if stack and "(" == stack[-1] :
                stack.pop()
            else :
                return False
    return True

def balance(x) :
    balance_dict = {'(':0, ")":0}
    for idx, char in enumerate(x) :
        balance_dict[char] += 1
        if balance_dict['('] == balance_dict[')'] :
            return x[:idx+1], x[idx+1:]

def trans(x) :
    ans = ''
    for i in x :
        if i == '(' :
            ans += ')'
        else :
            ans += '('
    return ans

def solution(p):
    if p == "":
        return ""
    
    u,v = balance(p)
    if right(u) :
        return u+solution(v)
    else :
        return '('+solution(v)+')'+ trans(u[1:-1])
