import heapq
def solution(scoville, K):
    answer = 0
    
    # 힙 정렬
    heapq.heapify(scoville)
    while scoville[0] < K:
        h1 = heapq.heappop(scoville)
        h2 = heapq.heappop(scoville)
        s = h1 + h2 * 2
        heapq.heappush(scoville,s)
        answer += 1
        
        # 모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
    return answer
