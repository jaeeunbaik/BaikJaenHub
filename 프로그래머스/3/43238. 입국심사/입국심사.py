def solution(n, times):
    answer = 0
    times.sort()
    left , right = times[0], times[0] * n
    while left < right:
        mid = (left + right) // 2
        total = 0
        for t in times:
            total += mid // t
        if total >= n:
            right = mid
        elif total < n:
            left = mid
        if left == right - 1:
            return right