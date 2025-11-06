def solution(array):
    result = [0]*1000
    
    for arr in array:
        result[arr] += 1
    
    cod = sorted(result, reverse=True)
    if cod[0] ==cod[1]:
        return -1
    
    return result.index(max(result))