def solution(arr):
    def step(a):
        res = []
        for v in a:
            if v >= 50 and v % 2 == 0:
                res.append(v // 2)
            elif v < 50 and v % 2 == 1:
                res.append(v * 2 + 1)
            else:
                res.append(v)
        return res

    x = 0
    cur = arr[:]
    while True:
        nxt = step(cur)
        if nxt == cur: 
            return x
        cur = nxt
        x += 1
