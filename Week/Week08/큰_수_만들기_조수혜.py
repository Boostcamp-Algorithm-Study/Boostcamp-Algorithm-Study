def solution(number, k):
    stack = []
    for num in number:
        # stack에 push되는 요소보다 stack에 존재하는 요소가 작은 경우 
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
            
        # number 차례대로 스택에 push
        stack.append(num)
        
    # 횟수가 남아있는 경우에는 뒤에서 삭제함
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
