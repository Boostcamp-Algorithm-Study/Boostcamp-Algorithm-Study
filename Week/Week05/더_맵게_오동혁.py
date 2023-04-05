import heapq


def solution(scoville, K):
    cnt = 0

    # heapq로 만들어 줌
    heapq.heapify(scoville)

    # 가장 작은 값이 K보다 작으면 음식을 섞음
    while scoville[0] < K:
        # 하지만 음식이 1개 밖에 안남았으면 -1을 return
        if len(scoville) == 1:
            return -1

        # 스코빌 지수가 가장 낮은 2개의 음식을 섞은 뒤, scoville에 넣음
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)

        heapq.heappush(scoville, food1 + food2*2)
        cnt += 1

    return cnt
