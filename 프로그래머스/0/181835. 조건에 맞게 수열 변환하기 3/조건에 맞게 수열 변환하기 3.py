def solution(arr, k):
    if k%2:
        return [a*k for a in arr]
    else:
        return [a+k for a in arr]