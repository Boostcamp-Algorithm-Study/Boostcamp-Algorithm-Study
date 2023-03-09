from collections import deque

queue = deque([i for i in range(1, int(input()) + 1)])

while queue:
    discard = queue.popleft()

    if queue:
        card = queue.popleft()
        queue.append(card)
    else:
        print(discard)
