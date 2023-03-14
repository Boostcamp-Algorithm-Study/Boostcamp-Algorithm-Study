from itertools import combinations
from collections import deque 

n, m = map(int, input("").split())
x = list(map(int, input("").split()))
t_cnt, true = x[0], x[1:]

visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]


party_list = []
for i in range(m) :
    p = list(map(int, input("").split()))
    p_cnt, party = p[0], p[1:]

    party_list.append(party)
    if p_cnt > 1 :
        tmp = list(combinations(party, 2))
        for a, b in tmp :
            graph[a].append(b) 
            graph[b].append(a)

if t_cnt == 0 :
    answer = m
else :
    answer = 0
    queue = deque(true)
    for q in queue :
        visited[q] = True
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
    idx_set = set([i for i,x in enumerate(visited) if x])

    for party in party_list :
        if len(set(party)) == len(set(party)-idx_set)  :
            answer +=1

print(answer)
