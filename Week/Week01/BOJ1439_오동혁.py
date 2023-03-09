import sys

input = sys.stdin.readline

s = list(map(int, input().rstrip()))

cnt = [0, 0]

cur = s[0]
cnt[cur] += 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        cur = (cur+1) % 2
        cnt[cur] += 1

print(min(cnt))
