def solution(num, total):
    start = (2 * total / num - (num - 1)) / 2
    return [int(start + i) for i in range(num)]
