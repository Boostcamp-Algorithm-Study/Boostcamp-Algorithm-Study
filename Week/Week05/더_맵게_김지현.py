from heapq import heapify, heappop, heappush

def solution(scoville, K):
    count = 0
    heapify(scoville) 
    a = heappop(scoville)
    
    while a < K :
        if not scoville :
            count = -1
            break
            
        b = heappop(scoville)
        heappush(scoville, a+2*b)
        count += 1
        
        a = heappop(scoville)
            
    return count 
