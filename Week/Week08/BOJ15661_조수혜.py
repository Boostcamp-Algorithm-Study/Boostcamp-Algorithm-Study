from itertools import combinations
N = int(input())
people = [i for i in range(N)]

graph = []
for _ in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    
# 리스트내의 원소를 돌면서 graph에서의 총합을 반환하는 함수 
def calculating(arr):
    total = 0
    # 리스트내에 원소가 존재할때까지
    while arr:
        x = arr.pop()
        # 예외처리
        if len(arr) >= 1:
            for y in arr:
                total += graph[x][y] + graph[y][x]
    return total    

answer = float('inf')
for i in range(1, N//2+1):
    # 가능한 모든 조합을 구함
    for arr in list(combinations(people, i)):
        start = list(arr)
        link = list(set(people)-set(arr))
        start_sum = calculating(start)
        link_sum = calculating(link)
        answer = min(answer, abs(link_sum - start_sum))
        if answer == 0:
            break
print(answer)
