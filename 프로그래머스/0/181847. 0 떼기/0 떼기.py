def solution(n_str):
    # result = ""
    # for i in range(len(n_str),-1,-1):
    #     if n_str.startswith("0"*i):
    #         result = n_str[i:]
    #         break
    # return result
    return n_str.lstrip('0')