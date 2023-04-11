def find(parent, x): 
  if parent[x] != x: 
    parent[x] = find(parent, parent[x])  
  return parent[x]

def union(parent, a, b): 
  a = find(parent, a) 
  b = find(parent, b) 
  if a < b: 
    parent[b] = a 
  else: 
    parent[a] = b 

n = int(input())  # 노드 개수  
m = int(input())  # 간선의 개수 

parent = [0] * (n + 1) 
edges = [] 
total_cost = 0 

for i in range(1, n+1):  # 부모노드를 자기자신으로 초기화
  parent[i] = i  

for _ in range(m): 
  a, b, cost = map(int, input().split()) 
  edges.append((cost, a, b)) 

edges.sort()  # 크루스칼 알고리즘 -> 그리디 

for edge in edges: 
    cost, a, b = edge 
    if find(parent, a) != find(parent, b):  # 사이클이 발생하지 않는다면  
      union(parent, a, b) 
      total_cost += cost 

print(total_cost) 
