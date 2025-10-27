def solution(order):
    return sum([1 if str(i) in "369" else 0 for i in str(order)])