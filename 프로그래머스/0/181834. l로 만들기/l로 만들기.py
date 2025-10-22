def solution(myString):
    ms = list(myString)
    result = ["l" if s<"l" else s for s in ms]
    return ''.join(result)