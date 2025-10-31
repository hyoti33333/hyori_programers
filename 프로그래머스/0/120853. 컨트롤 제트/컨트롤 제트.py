def solution(s):
    result = []
    for x in s.split():
        result.pop() if x == 'Z' else result.append(int(x))
    return sum(result)
