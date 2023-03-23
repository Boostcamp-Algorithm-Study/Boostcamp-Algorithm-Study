from itertools import permutations


def solution(k, dungeons):
    answer = 0
    cases = list(permutations(dungeons, len(dungeons)))

    for case in cases:
        total_fatique = k
        temp_cnt = 0
        for need_fatique, use_fatique in case:
            if total_fatique < need_fatique:
                break

            total_fatique -= use_fatique
            temp_cnt += 1

        answer = max(answer, temp_cnt)

    return answer
