import re
def solution(files):
    answer = []
    
    for i in files:
        # 숫자 추출
        number = re.findall('\d+', i)
        # 숫자를 기준으로 분할
        word = re.split('\d+', i)
        
        #tail 이 없는 경우
        if len(word) <=1:
            answer.append([word[0], number[0]])
        
        # tail이 존재하는 경우
        elif len(number)>=2:
            answer.append([word[0], number[0],i.replace(word[0],'',1).replace(number[0],'',1)])
        else:
            answer.append([word[0], number[0], word[1]])
        
    # 소문자로 변환
    answer.sort(key=lambda x:(x[0].lower(),int(x[1])))
    # 모든 리스트를 문자열로 변환 후 반환
    answer = [''.join(x) for x in answer]
    return answer
