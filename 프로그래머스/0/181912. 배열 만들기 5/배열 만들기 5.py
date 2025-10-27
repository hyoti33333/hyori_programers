def solution(intStrs, k, s, l):
    arr = [sa[s:s+l] for sa in intStrs]
    return [int(a) for a in arr if int(a)>k]