import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(i):
    # 만약 현재 노드가 지울 노드라면
    if i == node:
        return

    # 자신의 자식 노드가 1개 있는데 그게 지울 노드라면
    if tree[i] == [node]:
        result[i] += 1
        return

    # 자신이 leaf node인 경우
    if not tree[i]:
        result[i] = 1

    # 자식 노드가 있다면 다시 탐색
    for child_node in tree[i]:
        dfs(child_node)


n = int(input())

# parent[idx] -> idx번 노드의 부모 노드 값
parent = list(map(int, input().split()))

# 지울 노드의 번호
node = int(input())

tree = [[] for _ in range(n)]
visit = [False]*n
# leaf node인 노드 번호에는 1을 넣음
result = [0]*n

# 부모 노드가 존재하면 부모 노드 index에 자신을 추가
for i in range(n):
    if(parent[i] != -1):
        tree[parent[i]].append(i)

# root노드를 찾아서 root노드부터 시작
dfs(parent.index(-1))

print(sum(result))
