target, input_data = map(int, input().split())

result = 0
count = 0 
while input_data >= 0: 

  if str(input_data)[-1] == '1':
    if str(input_data)[:-1] == "": 
      result = -1
      break 
    input_data = int(str(input_data)[:-1])
  elif input_data % 2 == 0: 
    input_data = input_data // 2 
  else: 
    result = -1 
    break 
  
  count += 1
  if input_data == target:
    break

if result == -1: 
  print(result)
else: 
  print(count+1)
