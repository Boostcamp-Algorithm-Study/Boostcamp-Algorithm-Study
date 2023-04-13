from collections import deque 

N = int(input())  # 노드 개수 
parent_info = list(map(int, input().split())) 
removed = int(input()) 

tree = [[] for _ in range(N)] 
alive = [True for _ in range(N)] 
root = 0 

for i in range(N): 
    if parent_info[i] != -1: 
        tree[parent_info[i]].append(i)  # 자식 노드 추가 
    else:  # 루트 노드인 경우 
        root = i 

def bfs(p): 
    queue = deque([p]) 
    visited = [False for _ in range(N)] 
    visited[p] = True 
    alive[p] = False  

    while queue: 
        p = queue.popleft() 

        for child in tree[p]: 
            if not visited[child]: 
                queue.append(child) 
                visited[child] = True 
                alive[child] = False 

def solution(removed_node): 
    count = 0 
    alive[removed_node] = False 

    if removed_node == root: 
        return 0 
    elif len(tree[removed_node]) == 0:  # 자식 노드가 하나도 없는 경우 -> leaf node
        parent_index = 0 
        for i, parent in enumerate(tree):
            for child in parent: 
                if child == removed_node: 
                    parent_index = i  # 현재 확인하고 있는 child의 부모노드 = i 
        tree[parent_index].remove(removed_node)  # 부모 노드가 자식을 하나만 가지고 있는 경우 leaf node가 삭제되면 부모 노드가 leaf node가 된다
    else: 
        for child in tree[removed_node]: 
            bfs(child) 

    for i in range(N): 
        if alive[i] and len(tree[i]) == 0: 
            count += 1
    return count 

print(solution(removed))
