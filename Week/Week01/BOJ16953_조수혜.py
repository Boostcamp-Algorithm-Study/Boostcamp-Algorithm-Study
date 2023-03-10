a, b = map(int,input().split())
cnt = 1
    
while b > a:
    if a == b:
        break
    elif str(b)[-1] == '1':
        cnt += 1
        b = int(str(b)[:-1])
    elif b % 2 == 0:
        cnt += 1
        b = b //2
    else:
        break
        
if a == b:
    print(cnt)
else:
    print(-1)
