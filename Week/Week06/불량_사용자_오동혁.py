from itertools import permutations


def solution(user_id, banned_id):
    result = set()
    # 모든 경우의 수 판단
    perm = permutations(user_id, len(banned_id))

    # 두 id를 비교
    def compare(s1, s2):
        if(len(s1) != len(s2)):
            return False

        for c1, c2 in zip(s1, s2):
            if(c2 != '*' and c1 != c2):
                return False
        return True

    # 해당 경우의 수가 banned_id에 포함되는지 판단
    for l in list(perm):
        check = 0

        for idx in range(len(l)):
            if(not compare(l[idx], banned_id[idx])):
                check = 1
                break

        # 만약 현재의 경우가 banned_id에 포함된다면
        if(not check):
            l = tuple(sorted(l))
            result.add(l)

    return len(result)
