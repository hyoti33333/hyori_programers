def solution(n, control):
    opp = {"w":1,"s":-1,"d":10,"a":-10}
    for i in control:
        n+= opp[i] 
    return n