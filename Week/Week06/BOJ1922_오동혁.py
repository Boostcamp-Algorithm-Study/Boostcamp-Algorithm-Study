import sys
import heapq

# MST(Minimum Spanning Tree) 문제
# ST -> 최소 연결 부분 그래프 - 노드가 n개가 있으면 n-1개의 간선으로 연결된 트리 형태
# MST -> ST의 간선들의 가중치 합이 최소가 되는 트리
# MST의 특징
# 1. 간선의 가중치 합이 최소
# 2. n개의 노드를 가지는 그래프에서 n-1개의 간선만을 사용
# 3. 사이클이 포함되면 안됨

# 구현 방법
# 1. Kruskal 알고리즘 - 간선 선택 기반
#   - 간선 가중치를 오름차순으로 정렬
#   - 가장 낮은 가중치 선택 -> 사이클을 형성하는 간선이면 pass -> 사이클 형성은 Union-find 알고리즘을 통해 알 수 있음
#   - 해당 간선이 사이클을 형성하지 않으면 해당 간선을 사용
# 2. Prin 알고리즘 - 정점 선택 기반
#   - 시작 노드를 선택
#   - 현재까지 방문한 노드들에 연결된 모든 간선들 중에 가중치가 최소인 간선 선택 -> 이미 방문한 노드라면 pass
#   - 간선의 수가 n-1개가 될 때까지 반복

input = sys.stdin.readline

n = int(input())
m = int(input())
# 비용을 저장하는 딕셔너리
cost = dict()
# 해당 노드를 방문했는지 판단해주는 리스트
visit = [False]*(n+1)
# 간선의 수 -> 간선의 수가 n-1개가 최대가 되도록 한다
cnt = 0
# 최소 비용
result = 0

for i in range(1, n+1):
    cost[i] = dict()

for _ in range(m):
    f, t, c = map(int, input().split())

    cost[f][t] = c
    cost[t][f] = c

# 최소 스패닝 트리(MST) Prim 알고리즘 사용 -> heapq(우선순위 큐) 이용
queue = [(0, 1)]

while(cnt < n):
    c, node = heapq.heappop(queue)
    # 이미 방문한 노드인 경우
    if(visit[node]):
        continue
    # 노드를 방문했다고 해준 뒤, 결과값에 비용을 더해주고 간선이 하나 추가되었다고 해준다.
    visit[node] = True
    result += c
    cnt += 1

    for next_node, next_cost in cost[node].items():
        if(not visit[next_node]):
            heapq.heappush(queue, (next_cost, next_node))

print(result)
