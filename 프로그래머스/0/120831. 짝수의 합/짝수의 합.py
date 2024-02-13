def solution(n):
    even = list(range(n+1)[::2])
    return sum(even)