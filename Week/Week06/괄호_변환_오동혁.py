def solution(p):
    if not p:
        return ''

    answer = ''
    # p1은 '('의 수, p2는 ')'의 수
    p1 = 0
    p2 = 0

    for idx in range(len(p)):
        if p[idx] == '(':
            p1 += 1
        else:
            p2 += 1

        # 만약 '('의 수와 ')'의 수가 같다면 u, v로 분리
        if p1 == p2:
            u = p[:idx+1]
            v = p[idx+1:]
            break

        idx += 1

    # u가 올바른 문자열인지 판단
    if correct(u):
        answer = u + solution(v)
    # 올바른 문자열이 아니라면 처음부터 재귀적으로 실행
    else:
        answer = '(' + solution(v) + ')' + rever(u)

    return answer

# u가 올바른 문자열인지 판단


def correct(u):
    stack = []

    for i in u:
        if(i == '('):
            stack.append(i)
        elif(i == ')' and stack and stack[len(stack)-1] == '('):
            stack.pop()
        else:
            return False

    return True

# 4-4 실행


def rever(u):
    arr = list(u)
    arr.pop(0)
    arr.pop()

    temp = ''

    for i in arr:
        if(i == '('):
            temp += ')'
        else:
            temp += '('

    return temp
