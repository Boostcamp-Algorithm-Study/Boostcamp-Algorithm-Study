def solution(n):
    nums = []
    
    while n > 0 :    
        n, mod = divmod(n,3)
        nums.append(mod)
        if mod == 0 : 
            n -= 1
    
    nums = list(map(lambda x : '4' if x==0 else str(x), nums))
    answer = ''.join(nums[::-1])
    
    return answer
