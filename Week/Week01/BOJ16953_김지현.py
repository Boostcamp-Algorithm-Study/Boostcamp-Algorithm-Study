a, b = map(int,input("").split())
answer = 1

while True :
    if b == a :
        break
        
    x = b%10 
    if (x % 2 == 1 and x != 1) or (b < a) :
        answer = -1
        break

    elif x == 1 :
        b //= 10
        answer += 1
        
    else :
        b //= 2
        answer += 1

print(answer)
