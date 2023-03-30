def get_score(question, choice):
  left, right = question[0], question[1]

  type = question
  if choice == 4:
    score = 0
  elif choice < 4:
    score = 4 - choice
    type = left + right
  elif 4 < choice:
    score = choice - 4
    type = right + left

  return type, score


def solution(survey, choices):
  result = {
    "RT": 0,
    "TR": 0,
    "FC": 0,
    "CF": 0,
    "MJ": 0,
    "JM": 0,
    "AN": 0,
    "NA": 0
  }
  answer = ''

  for question, choice in zip(survey, choices):
    type, score = get_score(question, choice)

    result[type] += score

  answer += 'R' if result['RT'] >= result['TR'] else 'T'
  answer += 'C' if result['CF'] >= result['FC'] else 'F'
  answer += 'J' if result['JM'] >= result['MJ'] else 'M'
  answer += 'A' if result['AN'] >= result['NA'] else 'N'

  return answer