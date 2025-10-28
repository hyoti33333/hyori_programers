def solution(myString, pat):
    return sum([1 for i in range(len(myString)-len(pat)+1) if pat == myString[i:i+len(pat)]])