def solution(my_string):
    for ms in my_string:
        if ms.isalpha():
            my_string = my_string.replace(ms,' ')
    my_string = my_string.split()
    
    return sum(list(map(int,my_string)))