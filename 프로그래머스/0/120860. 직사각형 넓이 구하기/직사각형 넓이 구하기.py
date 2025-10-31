def solution(dots):
    xs , ys= [x for x, _ in dots], [y for _, y in dots]
    return (max(xs) - min(xs)) * (max(ys) - min(ys))