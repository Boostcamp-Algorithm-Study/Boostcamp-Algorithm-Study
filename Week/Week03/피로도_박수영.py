# method 1: using permutation of itertools
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    all_possible_case = list(permutations(dungeons))

    for case in all_possible_case:
        curr_fatigue = k
        num_explored_dungeons = 0

        for required, consumed in case:
            if required > curr_fatigue:
                continue

            curr_fatigue -= consumed
            num_explored_dungeons += 1

        answer = max(answer, num_explored_dungeons)

    return answer
    
if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))