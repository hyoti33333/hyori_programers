def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk ==[]:
            stk.append(arr[i])
            i += 1
        elif stk != [] and stk[-1] == arr[i]:
            del stk[-1]
            i += 1
        elif stk != [] and stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    if stk ==[]:
        return [-1]
    return stk
