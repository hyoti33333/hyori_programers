def solution(strArr):
    answer = [len(i) for i in strArr]
    cnt = 0
    for i in range(1,31):
        if cnt < answer.count(i):
            cnt = answer.count(i)
    
    return cnt