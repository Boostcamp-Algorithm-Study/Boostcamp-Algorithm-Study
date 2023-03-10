from collections import deque

n = int(input())
queue = deque(list(range(1,n+1)))

while len(queue) > 1:
    i = queue.popleft()
    queue.rotate(-1)
    
print(queue[0])
