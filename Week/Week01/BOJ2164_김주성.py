from collections import deque 

n = int(input())

q = deque() 
for x in range(1, n+1): 
  q.append(x) 

i = 1
while True: 

  now = q.popleft() 
  if i % 2 == 1: 
    pass   
  else: 
    q.append(now)
  
  i += 1

  if not len(q): 
    break  

print(now)