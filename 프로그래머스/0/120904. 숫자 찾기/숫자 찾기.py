def solution(num, k):
    num = str(num)
    
    for n in range(len(num)):
        if num[n] == str(k):
            return n+1
    return -1