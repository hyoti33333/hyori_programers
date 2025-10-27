def solution(arr):
    for i in range(10,1,-1):
        if len(arr)>2**i:
            for n in range(0, 2**(i+1)-len(arr)):
                arr.append(0)
    return arr