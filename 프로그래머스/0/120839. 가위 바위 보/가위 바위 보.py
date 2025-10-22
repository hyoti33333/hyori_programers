def solution(rsp):
    # 가위 2, 바위 0, 보 5
    dict = {"2":"0","0":"5","5":"2"}
    return "".join([dict[i] for i in rsp])