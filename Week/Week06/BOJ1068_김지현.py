# [-1,0,0,1,1] -> 해당 위치 노드들의 부모의 인덱스(-1 제외)를 의미
#   0,1,2,3,4  -> 노드들은 인덱스를 값으로 가짐

def delete(tree, out) :
    # 삭제되어야 할 노드의 부모를 -2로 설정
    tree[out] = -2
    
    # 부모가 삭제되어야 하는 값을 가진다면 삭제해야 함
    for node, parent in enumerate(tree) :
        if parent == out : 
            delete(tree, node)

# solution
N = int(input()) # 트리 노드 수
tree = list(map(int, input().split())) # 부모 노드의 번호 리스트
out = int(input()) # 지울 노드 번호

delete(tree, out)

answer = 0
for node in range(N) :
    parent = tree[node]
    
    # 삭제된 노드가 아니면서 다른 노드의 부모가 아닌 경우 리프노드로 간주
    if parent != -2 and node not in tree :
        answer += 1
        
print(answer)
