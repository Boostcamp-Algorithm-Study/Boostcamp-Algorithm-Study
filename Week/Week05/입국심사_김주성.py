def solution(n, times):
  answer = 0
  left, right = 1, max(times) * n

  while left <= right:
    # 현재 step에서는 mid 분에 대해서 판단
    mid = (left + right) // 2
    total_people = 0

    for time in times:
      # mid 분동안 심사 가능한 총 사람의 수
      total_people += mid // time

    if total_people >= n:  # 시간을 더 줄여도 됨
      answer = mid  # 최종적으로 최적의 시간을 구함
      right = mid - 1
    else:
      left = mid + 1

  return answer