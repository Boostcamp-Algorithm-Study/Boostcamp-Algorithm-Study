def solution(files):
    answer = []

    # 모든 파일을 돌면서 answer 배열에 [head, num, tail] 저장
    for file in files:
        # num구간의 인덱스를 구하기 위함
        num_start, num_end = 0, 0

        # num 구간 인덱스를 구함
        for idx, c in enumerate(file):
            if '0' <= c <= '9' and not num_start:
                num_start = idx
            elif num_start and not ('0' <= c <= '9'):
                num_end = idx
                break

        # 마지막까지 숫자가 이어진다면 num_end를 현재 file의 길이로
        if not num_end:
            num_end = len(file)

        answer.append(
            [file[:num_start], file[num_start:num_end], file[num_end:]])

    # answer에 들어간 값들을 [head, int(num)]으로 오름차순 정렬
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))

    # 각 값들을 문자열 하나로 합침
    return list(map(''.join, answer))
