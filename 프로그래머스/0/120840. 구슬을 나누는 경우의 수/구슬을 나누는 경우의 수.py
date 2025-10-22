def solution(balls, share):
    arr = [balls, balls-share, share]
    n = [1,1,1]
    for j in range(len(arr)):
        for i in range(arr[j],1,-1):
            n[j] *= i
    return n[0]/(n[1]*n[2])