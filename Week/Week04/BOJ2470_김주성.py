import sys 

n = int(input())  # 용액 수 
solutions = list(map(int, input().split()))  # 용액 특성값

solutions.sort()
start = 0
end = n-1
min_take = sys.maxsize 
# min_take = 1000000001

result = None 
while start < end:
    take = solutions[start] + solutions[end]  # 혼합 용액의 특성값
    if abs(take) < min_take:
        min_take = abs(take)
        result = [solutions[start], solutions[end]]
    if take < 0:
        start += 1
    elif take > 0:
        end -= 1
    else:  # 혼합 용액의 특성값이 0인 경우 
        break

print(result[0], result[1])