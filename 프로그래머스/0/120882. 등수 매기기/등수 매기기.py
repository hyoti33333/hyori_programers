def solution(score):
    avg = [sum(s)/2 for s in score]
    return [sum(i>a for i in avg)+1  for a in avg]
