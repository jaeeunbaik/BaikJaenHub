def solution(keyinput, board):
    loc = [0, 0]
    w = board[0]//2
    h = board[1]//2
    for key in keyinput:
        if key == "up" and loc[1] != h:
            loc[1] += 1
        elif key == "down" and loc[1] != -h:
            loc[1] -= 1
        elif key == "left" and loc[0] != -w:
            loc[0] -= 1
        elif key == "right" and loc[0] != w:
            loc[0] += 1
    return loc