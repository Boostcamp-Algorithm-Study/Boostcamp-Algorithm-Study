# setting
n = int(input(""))
nums = []
answer = []

# 입력 및 답을 저장할 리스트 선언
for i in range(n) :
    nums.append(list(map(int, input("").split())))
    answer.append([0]*(i+1))

# 계산
for i in range(n) :
    for j in range(i+1) :
        if j == 0 :
            answer[i][j] = nums[i][j] + answer[i-1][j]
        elif j == i :
            answer[i][j] = nums[i][j] + answer[i-1][j-1]
        else :
            answer[i][j] = max(answer[i-1][j], answer[i-1][j-1]) + nums[i][j]

# result
print(max(answer[-1]))
