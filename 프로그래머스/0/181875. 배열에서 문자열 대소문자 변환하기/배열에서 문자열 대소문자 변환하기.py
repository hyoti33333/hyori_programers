def solution(strArr):
    return [strArr[arr].upper() if arr%2 else strArr[arr].lower() for arr in range(len(strArr))]
