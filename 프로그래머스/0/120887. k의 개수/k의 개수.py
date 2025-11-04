def solution(i, j, k):
    target = str(k) 
    return sum([str(num).count(target) for num in range(i,j+1)])
