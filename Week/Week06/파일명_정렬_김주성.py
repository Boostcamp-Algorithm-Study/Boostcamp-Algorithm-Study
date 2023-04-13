def solution(files):
    tmp = [] 
    head, number, tail = '', '', '' 
    
    for file in files: 
        for i in range(len(file)): 
            if file[i].isdigit(): 
                head = file[:i] 
                number = file[i:] 
                
                for j in range(len(number)): 
                    if not number[j].isdigit(): 
                        tail = number[j:] 
                        number = number[:j] 
                        break 
                        
                tmp.append([head, number, tail]) 
                head, number, tail = '', '', '' 
                break 
                
    tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1])))  # (head, number) <- stable 정렬이므로 원래의 상대적인 순서 유지
    
    return [''.join(i) for i in tmp] 