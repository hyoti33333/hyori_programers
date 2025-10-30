def solution(rank, attendance):
    students = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    students.sort()
    a, b, c = [students[i][1] for i in range(3)]
    return 10000 * a + 100 * b + c
    