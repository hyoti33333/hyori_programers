def solution(my_string):
    answer = [0]*52
    for st in my_string:
        if 'A' <= st <='Z':
            answer[ord(st)-ord('A')] +=1
        elif 'a' <= st <= 'z':
            answer[26+ord(st)-ord('a')] += 1
    return answer