def solution(order):
    answer = 0
    for s in str(order):
        if s == '3' or s=='6' or s=='9':
            answer += 1
    return answer