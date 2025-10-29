def solution(arr, flag):
    x = []
    for i in range(len(flag)):
        if flag[i]:
            x.extend([arr[i]] * (arr[i] * 2))
        else:
            del x[-arr[i]:]
    return x
   