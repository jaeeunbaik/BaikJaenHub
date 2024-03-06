def solution(n):
    i = 1
    fac = 1
    while True:
        fac *= i
        if fac > n:
            break
        i += 1
    return i-1