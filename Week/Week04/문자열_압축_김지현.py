def solution(s):
    answer_length = float('inf')
    
    for length in range(1,len(s)+1) : # 단위 설정
        result_length = 0
        prev_str = ''
        count = 1
        
        for i in range(0,len(s)+length,length) : # 문자열을 단위만큼 잘라서 확인
            curr_str = s[i:i+length] 
            if prev_str == curr_str : 
                count += 1
            else : 
                if count == 1 :
                    result_length += len(curr_str)
                else :
                    result_length += (len(str(count))+len(curr_str))
                count = 1
            prev_str = curr_str
            
        answer_length = min(answer_length, result_length)
        
    return answer_length
