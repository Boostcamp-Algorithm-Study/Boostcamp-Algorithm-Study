# n개의 물건, 최대 무게 k
n, k = map(int, input("").split())

# 각 물건의 무게와 가치
weight_value = []
for i in range(n) :
    weight_value.append(list(map(int, input("").split())))

weight_value.sort(key=lambda x : (-x[0], -x[1]))

# 각 무게 별 최대 가치를 저장하는 리스트
bag = [0 for _ in range(k+1)]

for weight, value in weight_value :
    for i in range(k, weight-1,-1) :
        bag[i] = max(bag[i], value+bag[i-weight])
        
print(max(bag))
