def solution(my_string, indices):
    my_string = list(my_string)
    idx = sorted(indices, reverse=True)
    for i in idx:
        del my_string[i]
    return ''.join(my_string)