def solution(quiz):
    result = []
    for q in quiz:
        a, b = q.split('=')
        if eval(a) == int(b):
            result.append("O")
        else: 
            result.append("X")
    return result