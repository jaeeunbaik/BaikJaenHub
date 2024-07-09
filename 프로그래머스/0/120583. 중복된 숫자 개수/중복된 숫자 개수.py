def solution(array, n):
    cnt = 0
    for num in array:
        if num == n:
            cnt += 1
    return cnt            
