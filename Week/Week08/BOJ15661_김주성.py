from itertools import combinations
import math

def cal_ability(team):
  ability = 0
  for i in team:
    for j in team:
      if i == j:
        continue
      ability += table[i][j]
  return ability


n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

people = range(n)
cases = combinations(list(people), n // 2)

min_ = math.inf
for star in cases:
  link = [p for p in people if p not in star]

  diff = abs(cal_ability(star) - cal_ability(link))
  min_ = min(diff, min_)

print(min_)
