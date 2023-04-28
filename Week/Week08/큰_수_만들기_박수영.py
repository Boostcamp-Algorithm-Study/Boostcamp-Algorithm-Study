def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    
    return ''.join(stack)

if __name__ == "__main__":
    print(solution("1924", 2))
    print(solution("1231234", 3))
    print(solution("4177252841", 4))