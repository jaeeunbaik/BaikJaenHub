def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n != 0:
            answer.append(num)
    return [n for n in numlist if n not in answer]