import sys

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

# index
left = 0
right = N-1

x = sys.maxsize
answer = []

while left < right:
    left_ = arr[left]
    right_ = arr[right]
    
    total = left_ + right_
    
    # 0에 더 가까운 값을 정답 리스트에 추가함
    if abs(total) < x:
        answer = [left_, right_]
        x = abs(total)
        
    # 더한 값이 0보다 작으면 왼쪽 값을 늘려 0에 가깝게 이동
    if total < 0:
        left += 1
    
    # 더한 값이 0보다 크면 오른쪽값을 줄여 0에 가깝게 이동
    elif total > 0:
        right -= 1
        
    else:
        break

print(answer[0], answer[1])
