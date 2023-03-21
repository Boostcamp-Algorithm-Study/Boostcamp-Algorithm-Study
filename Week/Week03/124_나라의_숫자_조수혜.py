def solution(n):
    answer = ''
    nums = [1,2,4]
    
    while n > 0:
        n -= 1
        n, v = divmod(n,3)
        answer += str(nums[v])
    return answer[::-1]
