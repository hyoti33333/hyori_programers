def solution(n):
    count = []
    for i in range(1,n+1):
        num = 0
        for j in range(1,i+1):
            if i%j==0:
                num += 1
        if num>=3:
            count.append(i)
    return len(count)