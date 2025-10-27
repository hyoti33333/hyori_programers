def solution(myString):
    arr = myString.split('x')
    answer = [a for a in arr if a!=""]
    return sorted(answer)