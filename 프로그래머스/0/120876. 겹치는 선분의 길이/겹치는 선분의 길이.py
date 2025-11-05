def solution(lines):
    arr = [0] * 201

    for start, end in lines:
        for x in range(start, end):
            arr[x + 100] += 1
    return sum(1 for c in arr if c >= 2)
