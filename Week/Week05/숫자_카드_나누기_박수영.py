# time: 1hr 55m
import math

def get_gcd(arr):
    arr.sort()
    gcd = arr[0]
    for val in arr:
        gcd = math.gcd(gcd, val)
    
    return gcd

def check(denomiator, arr):
    flag = True
    for val in arr:
        if (val % denomiator) == 0:
            flag = False
            break
    
    return denomiator if flag else 0

def solution(arrayA, arrayB):
    answer = 0
    gcd_a, gcd_b = get_gcd(arrayA), get_gcd(arrayB)

    if gcd_a != 1:  # 조건 1 확인
        answer = max(answer, check(gcd_a, arrayB))
    
    if gcd_b != 1:  # 조건 2 확인
        answer = max(answer, check(gcd_b, arrayA))    
    
    return answer

if __name__ == "__main__":
    print(solution([10, 17], [5, 20]))
    print(solution([10, 20], [5, 17]))
    print(solution([14, 35, 119], [18, 30, 102]))
