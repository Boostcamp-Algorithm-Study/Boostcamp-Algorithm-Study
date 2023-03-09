from sys import stdin

# 입력부
S = stdin.readline().strip()

# 알고리즘
if len(set(list(S))) == 1:
    print(0)
else:
    zeros, ones = [], []
    tmp = []
    for ch in S:
        if tmp:
            if tmp[-1] == ch:
                tmp.append(ch)

            else:
                if tmp[-1] == '0':
                    zeros.append(''.join(tmp))

                elif tmp[-1] == '1':
                    ones.append(''.join(tmp))
                tmp = [ch]
                    
        else:
            tmp.append(ch)
    
    if tmp:
        if tmp[-1] == '0':
            zeros.append(''.join(tmp))
        else:
            ones.append(''.join(tmp))

    print(min(len(zeros), len(ones)))