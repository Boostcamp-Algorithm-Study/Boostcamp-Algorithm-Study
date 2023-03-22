# 입력
n,m,r = map(int, input('').split())
boxs = min(n,m)//2

arr = []
for i in range(n) :
    arr.append(list(map(int, input('').split())))

# rotate
for i in range(r) :
    for i in range(boxs) :
        n_lim, m_lim = n-i, m-i
        value = arr[i][i]

        # 아래로 이동
        for j in range(i+1, n_lim) : 
            temp = arr[j][i]
            arr[j][i] = value
            value = temp

        # 오른쪽으로 이동
        for j in range(i+1, m_lim) :
            temp = arr[n_lim-1][j]
            arr[n_lim-1][j] = value
            value = temp
        
        # 위로 이동
        for j in range(n_lim-1, i, -1) :
            temp = arr[j-1][m_lim-1]
            arr[j-1][m_lim-1] = value
            value = temp

        # 왼쪽으로 이동
        for j in range(m_lim-1,i,-1) :
            temp = arr[i][j-1]
            arr[i][j-1] = value
            value = temp

# 정답 출력
for x in arr :
    print(*x)
