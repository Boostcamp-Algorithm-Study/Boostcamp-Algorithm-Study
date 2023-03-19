import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

# 길들을 저장해주는 dictionary
# paths[i][j] - i노드에서 j노드를 가는데 필요한 여물의 수
paths = defaultdict(lambda: defaultdict(lambda: float('inf')))

# 길을 입력 받을 때, 중복된 길이 나올수도 있으니 defaultdict 초기값을 무한대로 설정한 뒤에 가장 여물이 적게 필요한 경우로 저장
for _ in range(m):
    node1, node2, k = map(int, input().split())

    paths[node1][node2] = min(paths[node1][node2], k)
    paths[node2][node1] = min(paths[node2][node1], k)

# 1번 노드부터 각 노드까지 가는데 필요한 여물의 최소의 경우
dist = [float('inf')]*(n+1)

# 노드 1번에서 출발
queue = [(0, 1)]

while queue:
    cur_cnt, cur_node = heapq.heappop(queue)

    # 현재 노드가 n번 노드에 도착하면 while문을 빠져나감
    if cur_node == n:
        print(cur_cnt)
        exit(0)

    # 다음 노드로 가는데 필요한 여물의 수를 확인한 뒤에 dist배열과 비교해 현재 노드에서 다음 노드로
    # 넘어가는 경우에 여물이 더 적게 필요하면 dist를 최신화 해준 뒤, 최소 힙에 넣어준다.
    for next_node, k in paths[cur_node].items():
        next_cnt = cur_cnt + k

        if next_cnt < dist[next_node]:
            dist[next_node] = next_cnt
            heapq.heappush(queue, (next_cnt, next_node))
