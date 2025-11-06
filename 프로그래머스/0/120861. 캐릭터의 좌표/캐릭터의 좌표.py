def solution(keyinput, board):
    cod = [board[0] // 2, board[1] // 2]
    start = [0, 0]

    for i in keyinput:
        if i == 'up':
            start[1] += 1
        elif i == 'down':
            start[1] -= 1
        elif i == 'left':
            start[0] -= 1
        elif i == 'right':
            start[0] += 1

        if start[0] > cod[0]:
            start[0] = cod[0]
        elif start[0] < -cod[0]:
            start[0] = -cod[0]


        if start[1] > cod[1]:
            start[1] = cod[1]
        elif start[1] < -cod[1]:
            start[1] = -cod[1]

    return start
