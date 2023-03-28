def solution(s):
    # 최종 결과 값
    answer = len(s)

    # 문자열은 원래 길이 // 2보다 크게 자를 수는 없다.
    for i in range(1, len(s)//2 + 1):
        # i개 단위로 자른 첫 번째 문자열
        temp_str = s[:i]
        # i개 단위로 자를 경우 압축된 문자열
        i_result = ''
        # 잘린 이전 문자열들과 몇 번 연속으로 동일한지(?)
        cnt = 1

        # i개 단위로 자른 문자열들을 압축한다
        for j in range(1, len(s)//i):
            # 현재 문자열
            cur_str = s[i*j:i*(j+1)]

            # 만약 현재 문자열이 앞의 문자열과 같은 경우
            if temp_str == cur_str:
                cnt += 1
            # 앞의 문자열과 다른 경우 앞의 문자열들을 압축해준다
            else:
                # 반복 횟수가 1번보다 많다면 숫자와 합께 압축
                if cnt != 1:
                    i_result += str(cnt)

                # 문자열을 더해주고 temp_str을 업데이트해주고 cnt를 다시 1로 변경
                i_result += temp_str
                temp_str = cur_str
                cnt = 1

        # 마지막에 압축되지 못한 문자열을 압축
        if cnt > 1:
            i_result += str(cnt)

        i_result += temp_str

        if len(s) % i:
            i_result += s[i*(j+1):]

        answer = min(answer, len(i_result))

    return answer
