def solution(number, k):
    # 가장 큰 수를 만드는 배열
    answer = []

    # number의 숫자가 answer 배열의 가장 마지막 값과 비교
    for i in range(len(number)):
        # 만약 제거 가능한 숫자가 더이상 없을 때는 나머지 값을 모두 answer에 넣어준다.
        if not k:
            answer.append(number[i:])
            break

        cur = number[i]

        # answer배열에 값이 있고, 마지막 값이 현재 값보다 작고 제거 가능하다면(k가 0보다 크다면) answer의 마지막 값을 빼고, 제거 가능한 숫자의 수를 1 줄여줌
        # 이렇게 되면 값이 가장 수들을 가장 앞으로 보낼 수 있음.
        while answer and answer[-1] < cur and k:
            answer.pop()
            k -= 1

        answer.append(cur)

    # 만약 아직 제거해야되는 숫자가 k개가 있다면 뒤에서 부터 k개를 제거해줌
    for _ in range(k):
        answer.pop()

    return ''.join(answer)
