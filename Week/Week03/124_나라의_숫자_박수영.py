def decimal_to_124(num_decimal: int, cvt_rule='124'):
    div, mod = divmod(num_decimal, len(cvt_rule))
    if mod == 0:
        div -= 1
        mod = len(cvt_rule)
    
    return div, cvt_rule[mod-1]


def solution(n):
    answer = []
    rule = '124'
    
    if n <= len(rule):
        _, cvt_result = decimal_to_124(n)
        answer.append(cvt_result)
    else:
        share, cvt_result = decimal_to_124(n)
        answer.append(cvt_result)

        while share > len(rule):
            share, cvt_result = decimal_to_124(share)
            answer.append(cvt_result)

        answer.append(rule[share-1])


    return ''.join(answer[::-1])


if __name__ == '__main__':
    for i in range(1, 21):
        print(solution(i))