def solution(a, b):
    answer = 0
    data1 = int(str(a)+str(b))
    data2 = 2*a*b
    answer = data1 if data1>data2 else data2
    return answer