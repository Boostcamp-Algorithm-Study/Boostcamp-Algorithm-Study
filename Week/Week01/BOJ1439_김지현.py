s = input("")

nums = [0,0] 

x = int(s[0])
nums[x] += 1

for i in s[1:] :
    if int(i) != x : 
        x = int(i)
        nums[x] += 1

print(min(nums))
