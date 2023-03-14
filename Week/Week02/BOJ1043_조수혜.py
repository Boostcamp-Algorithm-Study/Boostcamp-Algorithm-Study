n, m = map(int, (input().split(' ')))
known_list = set(list(map(int,input().split(' ')))[1:])

parties = []

for _ in range(m):
    party = list(map(int, input().split(' ')))[1:]
    parties.append(party)

if len(known_list) == 0:
    print(m)
    
else:
    cnt = [False] * m
    for _ in range(m):
        for i,party in enumerate(parties):
            party = set(party)
            if len(party & known_list) >= 1:
                cnt[i] = True
                known_list.update(party)
        
    print(cnt.count(False))
