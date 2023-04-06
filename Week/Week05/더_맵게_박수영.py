import heapq

def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap)
    
    answer = 0
    if heap[0] >= K:
        return answer
    
    while len(heap) > 1:
        food_1, food_2 = heapq.heappop(heap), heapq.heappop(heap)
        heapq.heappush(heap, food_1 + food_2 * 2)
        answer += 1
        
        if heap[0] >= K:
            return answer
    
    return -1

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))