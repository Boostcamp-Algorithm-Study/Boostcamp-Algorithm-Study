# 구현 > 문제 이해를 잘하자
# time: 1hr
from collections import deque

def is_correct(p):
    tmp = deque(list(p))
    l_brackets = []
    flag = True
    while tmp:
        curr_bracket = tmp.popleft()
        if curr_bracket == "(":
            l_brackets.append(curr_bracket)
            continue
        
        # 현재 문자가 ")"인 경우
        if l_brackets: # "("가 존재한다면
            l_brackets.pop() # 매칭되었으므로 pop
        else: # 문자가 남았는데도 "("가 없다면
            flag = False # 올바른 괄호 문자열이 아님
            break
    
    return flag                


def brackets_to_uv(p):
    tmp = deque(list(p)) # ch 단위로 분리
    
    l_cnt, r_cnt = 0, 0
    u = []
    while tmp:
        u.append(tmp.popleft())
        if u[-1] == "(":
            l_cnt += 1
        elif u[-1] == ")":
            r_cnt += 1
        
        if l_cnt == r_cnt:
            break
    
    return (''.join(u), ''.join(tmp))

def reverse(p):
    tmp = deque(list(p))
    result = []
    while tmp:
        curr = tmp.popleft()
        if curr == "(":
            result.append(")")
        else:
            result.append("(")
    
    return ''.join(result)

def balance_to_both(p):
    # 1번 과정
    if not p:
        return ""
    
    # 2번 과정
    u, v = brackets_to_uv(p)
    
    # 3번 과정
    if is_correct(u):
        u += balance_to_both(v) # 3-1번 과정
    else:
        tmp = "("
        tmp += balance_to_both(v)
        tmp += ")"
        tmp += reverse(u[1:len(u)-1])
        
        return tmp
    
    return u

def solution(p):
    answer = balance_to_both(p)
    
    return p if not answer else answer


if __name__ == "__main__":
    print(solution("(()())()") == "(()())()")
    print(solution(")(")=="()")
    print(solution("()))((()")=="()(())()")