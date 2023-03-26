import sys

input = sys.stdin.readline

n = int(input())

liquid = sorted(list(map(int, input().split())))

# 현재 왼쪽, 오른쪽 인덱스
left, right = 0, n-1
# 현재까지 용액 합의 절대값 최소값
cur_min = float('inf')

# 정답 왼쪽, 오른쪽 인덱스
ans_left, ans_right = 0, n-1

# 용액 합이 0이 되거나, left인덱스가 right 인덱스보다 크거나 같으면 while문을 빠져나옴
while left < right:
    # 현재 두 용액의 합
    cur_sum = liquid[left] + liquid[right]

    # 용액 합의 절대값이 cur_min보다 작으면 최신화
    if abs(cur_sum) < cur_min:
        cur_min = abs(cur_sum)
        ans_left, ans_right = left, right

    # 용액 합이 0이면 while문을 빠져나옴
    if cur_sum == 0:
        break
    # 0보다 작으면 왼쪽 인덱스를 하나 오른쪽으로
    elif cur_sum < 0:
        left += 1
    # 0보다 크면 오른쪽 인덱스를 하나 왼쪽으로
    else:
        right -= 1

print(liquid[ans_left], liquid[ans_right])
