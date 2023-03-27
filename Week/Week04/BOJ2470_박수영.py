def formatting(vals: list)-> str:
    return ' '.join([str(x) for x in vals])

def answer(n: int, values: list)-> str:
    values = sorted(values)
    if n == 2:
        return formatting(values)
    
    # 포인터 두 개를 사용해서, 전체 탐색
    combs, hap = [], float('inf')
    pos_1, pos_2 = 0, n - 1
    while pos_1 < pos_2:
        candidate = [values[pos_1], values[pos_2]]
        
        # 조건 만족시 최소값 업데이트
        if abs(sum(candidate)) <= abs(hap):
            combs = candidate
            hap = sum(combs)
        
        # 포인터 업데이트
        if sum(candidate) == 0:
            break
        elif sum(candidate) < 0:
            pos_1 += 1
        else:
            pos_2 -= 1


    return formatting(combs)  


# 스크립트
if __name__ == '__main__':
    import sys

    # 입력
    n = int(input())
    specific_values = list(map(int, sys.stdin.readline().strip().split()))

    output = answer(n, specific_values)
    print(output)
