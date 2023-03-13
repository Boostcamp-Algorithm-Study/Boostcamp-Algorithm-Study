import sys

def unpacking(a, *args):
    return (a, set(args))

# 입력부
total_people, total_party  = map(int, sys.stdin.readline().split())
total_truth, num_of_truth = unpacking(*sys.stdin.readline().split())

parties = []
for _ in range(total_party):
    _, num_of_participant = unpacking(*sys.stdin.readline().split())
    parties.append(num_of_participant)

    
# 알고리즘
for _ in range(total_party):
    # print(f'num of truth: {num_of_truth}')
    for participant in parties:
        # print(f'participant: {participant}')
        if num_of_truth & set(participant):
            num_of_truth.update(participant)

answer = 0
for participant in parties: # 최종 확인
    if not num_of_truth & set(participant):
        answer += 1

print(answer)
