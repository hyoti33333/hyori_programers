def solution(arr, queries):
    for q in queries:
        for s in range(q[0],q[1]+1):
            arr[s] += 1
    return arr
