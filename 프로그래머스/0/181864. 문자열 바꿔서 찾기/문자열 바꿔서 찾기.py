def solution(myString, pat):
    myString = list(myString)
    myString = ["B" if s=="A" else "A" for s in myString ]
    myString= ''.join(myString)
    if pat in myString:
        return 1
    else:
        return 0