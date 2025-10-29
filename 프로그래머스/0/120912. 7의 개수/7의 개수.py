def solution(array):
    arr = ''.join(map(str,array))
    return sum([1 for i in arr if i==str(7)])