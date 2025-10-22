def solution(my_string):
    answer = [int(s) for s in my_string if not s.isalpha()]
    return sorted(answer)