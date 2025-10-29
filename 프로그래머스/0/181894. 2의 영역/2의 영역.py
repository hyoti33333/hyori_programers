def solution(arr):
    if 2 not in arr: return [-1]
    two = [i for i in range(len(arr)) if arr[i]==2]
    return arr[min(two):max(two)+1]