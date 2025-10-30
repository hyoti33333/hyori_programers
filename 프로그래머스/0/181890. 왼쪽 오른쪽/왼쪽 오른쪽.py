def solution(str_list):
    for i, sl in enumerate(str_list):
        if sl == 'l':
            return str_list[:i]
        elif sl == 'r':
            return str_list[i+1:]
    return []
