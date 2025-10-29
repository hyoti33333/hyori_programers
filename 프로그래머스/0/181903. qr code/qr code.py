def solution(q, r, code):
    return ''.join([code[c] for c in range(len(code)) if c%q == r])