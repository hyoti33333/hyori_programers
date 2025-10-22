def solution(my_string):
    word = 'aeiou'
    for w in word:
        my_string = my_string.replace(w,'')
    return my_string 