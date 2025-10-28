def solution(my_string):
    arr = ''.join([ ms if ms.isdecimal() else ' ' for ms in my_string ]).split()
    return  sum(list(map(int,arr)))