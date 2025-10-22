def solution(my_string):
    ms = my_string.split(' ')
    return [ms[i] for i in range(len(ms)) if ms[i] not in ' ']