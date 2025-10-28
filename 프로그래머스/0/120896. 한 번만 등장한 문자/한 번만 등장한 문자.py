def solution(s):
    answer = [s[st] for st in range(len(s)) if s[st] not in s[:st]+s[st+1:]] 
    return ''.join(sorted(answer))