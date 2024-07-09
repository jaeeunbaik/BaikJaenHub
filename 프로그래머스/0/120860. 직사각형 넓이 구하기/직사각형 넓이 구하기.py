def solution(dots):
    d = sorted(dots)
    y = abs(d[0][1] - d[1][1])
    x = abs(d[2][0] - d[0][0])
    return x*y