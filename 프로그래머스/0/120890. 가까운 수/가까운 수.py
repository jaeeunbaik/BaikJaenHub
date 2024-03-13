def solution(array, n):
    answer = []
    diff = 101
    for a in array:
        if abs(a - n) < diff:
            answer = [a]
            diff = abs(a-n)
        elif abs(a - n) == diff:
            answer.append(a)
    return min(answer)