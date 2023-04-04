import math
def gcd_n(arr):
    gcd = arr[0]
    for i in arr:
        gcd = math.gcd(gcd, i)
    return gcd

def solution(arrayA, arrayB):
    a = gcd_n(arrayA)
    b = gcd_n(arrayB)
    
    for i in arrayB:
        if i % a == 0:
            a = 0
            break
    for i in arrayA:
        if i % b == 0:
            b = 0
            break
    
    return max(a,b)
