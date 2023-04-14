# time: 1h 30m

from collections import deque

def get_divided(file: str):
    head, num, tail = [], [], []
    dq = deque(list(file))
    while dq:
        ch = dq.popleft()
        
        if not ch.isdigit() and not num:
            head.append(ch)
        elif ch.isdigit() and (len(num) < 5) and not tail:
            num.append(ch)
        else:
            tail.append(ch)
        
    return (''.join(head), ''.join(num), ''.join(tail))    
    

def solution(files):
    answer = []
    if len(files) == 1:
        return files
    
    dictionary = []
    for file in files:
        # 1. file을 head, num, tail로 분리
        results = get_divided(file)
        dictionary.append(results)
    
    answer = [''.join(x) for x in sorted(dictionary, key=lambda x: (x[0].lower(), x[1].zfill(5)))]
    
    return answer

if __name__ == "__main__":
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))