def solution(n, k):
    answer = []
    num = k
    while num <=n:
        answer.append(num)
        num += k
    return answer