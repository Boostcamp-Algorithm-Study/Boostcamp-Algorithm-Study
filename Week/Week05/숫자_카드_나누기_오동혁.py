def solution(arrayA, arrayB):
    answer = 0
    # 각 배열의 최솟값을 찾음 -> 최솟값보다 크게 되면 해당 배열에서 나눠 떨어지지않는 수가 존재
    min_A = min(arrayA)
    min_B = min(arrayB)

    # 각 배열의 최솟값의 약수들을 각 배열에 저장
    divisor_A = [min_A]
    divisor_B = [min_B]

    for i in range(2, int(min_A ** 0.5) + 1):
        if min_A % i == 0:
            divisor_A.append(i)
            divisor_A.append(min_A // i)

    for i in range(2, int(min_B ** 0.5) + 1):
        if min_B % i == 0:
            divisor_B.append(i)
            divisor_B.append(min_B // i)

    # 역순으로 정렬
    divisor_A.sort(reverse=True)
    divisor_B.sort(reverse=True)

    # 2가지 조건에 대해 각 최대값을 찾은 뒤, 그 값들 중에 최대값을 return
    for num in divisor_A:
        able = True

        # 1번 조건을 만족하는지 판단
        for a, b in zip(arrayA, arrayB):
            if a % num != 0 or b % num == 0:
                able = False
                break

        if able:
            answer = num
            break

    for num in divisor_B:
        able = True

        # 2번 조건을 만족하는지 판단
        for a, b in zip(arrayA, arrayB):
            if a % num == 0 or b % num != 0:
                able = False
                break

        if able:
            answer = max(answer, num)
            break

    return answer
